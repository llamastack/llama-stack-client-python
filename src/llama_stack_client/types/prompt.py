# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["Prompt"]


class Prompt(BaseModel):
    is_default: bool
    """Boolean indicating whether this version is the default version for this prompt"""

    prompt_id: str
    """Unique identifier formatted as 'pmpt\\__<48-digit-hash>'"""

    variables: List[str]
    """List of prompt variable names that can be used in the prompt template"""

    version: int
    """Version (integer starting at 1, incremented on save)"""

    prompt: Optional[str] = None
    """The system prompt text with variable placeholders.

    Variables are only supported when using the Responses API.
    """
