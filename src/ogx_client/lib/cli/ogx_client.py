# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

from __future__ import annotations

import os
import json
from importlib.metadata import version

import yaml
import click

from ogx_client import OgxClient

from .eval import eval
from .models import models
from .inspect import inspect
from .shields import shields
from .datasets import datasets
from .configure import configure
from .constants import get_config_file_path
from .inference import inference
from .providers import providers
from .eval_tasks import eval_tasks
from .vector_stores import vector_stores
from .scoring_functions import scoring_functions


@click.group()
@click.help_option("-h", "--help")
@click.version_option(version=version("ogx_client"), prog_name="ogx-client")
@click.option("--endpoint", type=str, help="OGX server endpoint", default="")
@click.option("--api-key", type=str, help="OGX server API key", default="")
@click.option("--config", type=str, help="Path to config file", default=None)
@click.pass_context
def ogx_client(ctx, endpoint: str, api_key: str, config: str | None):
    """Welcome to the ogx-client CLI - a command-line interface for interacting with an OGX server"""
    ctx.ensure_object(dict)

    if config and endpoint:
        raise ValueError("Cannot use both config and endpoint")

    if config is None:
        default_config = get_config_file_path()
        if default_config.exists():
            config = str(default_config)

    if config:
        try:
            with open(config, "r") as f:
                config_dict = yaml.safe_load(f)
                endpoint = config_dict.get("endpoint", endpoint)
                api_key = config_dict.get("api_key", "")
        except Exception as e:
            click.echo(f"Error loading config from {config}: {str(e)}", err=True)
            click.echo("Falling back to HTTP client with endpoint", err=True)

    if endpoint == "":
        endpoint = "http://localhost:8321"

    default_headers: dict[str, str] = {}
    if api_key != "":
        default_headers["Authorization"] = f"Bearer {api_key}"

    provider_data = {
        k: v
        for k, v in {
            "fireworks_api_key": os.environ.get("FIREWORKS_API_KEY", ""),
            "together_api_key": os.environ.get("TOGETHER_API_KEY", ""),
            "openai_api_key": os.environ.get("OPENAI_API_KEY", ""),
        }.items()
        if v
    }
    if provider_data:
        default_headers["X-OGX-Provider-Data"] = json.dumps(provider_data)

    client = OgxClient(
        base_url=endpoint,
        api_key=api_key or None,
        default_headers=default_headers,
    )
    ctx.obj = {"client": client}


ogx_client.add_command(models, "models")
ogx_client.add_command(vector_stores, "vector_stores")
ogx_client.add_command(shields, "shields")
ogx_client.add_command(eval_tasks, "eval_tasks")
ogx_client.add_command(providers, "providers")
ogx_client.add_command(datasets, "datasets")
ogx_client.add_command(configure, "configure")
ogx_client.add_command(scoring_functions, "scoring_functions")
ogx_client.add_command(eval, "eval")
ogx_client.add_command(inference, "inference")
ogx_client.add_command(inspect, "inspect")


def main():
    ogx_client()


if __name__ == "__main__":
    main()
