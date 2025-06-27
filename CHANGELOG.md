# Changelog

## 0.1.0-alpha.4 (2025-06-27)

Full Changelog: [v0.1.0-alpha.3...v0.1.0-alpha.4](https://github.com/llamastack/llama-stack-client-python/compare/v0.1.0-alpha.3...v0.1.0-alpha.4)

### Features

* **api:** update via SDK Studio ([4333cb0](https://github.com/llamastack/llama-stack-client-python/commit/4333cb0307fd99654e53e8f87b3b2951be027b44))


### Bug Fixes

* **ci:** update pyproject.toml to use uv and remove broken CI ([#5](https://github.com/llamastack/llama-stack-client-python/issues/5)) ([7bc925c](https://github.com/llamastack/llama-stack-client-python/commit/7bc925c00401799d8f3345a4873f1b0028cb45ea))


### Chores

* **internal:** version bump ([867ea24](https://github.com/llamastack/llama-stack-client-python/commit/867ea24344fd71fc9787807a47144af5e3de82f8))

## 0.1.0-alpha.3 (2025-06-27)

Full Changelog: [v0.1.0-alpha.2...v0.1.0-alpha.3](https://github.com/llamastack/llama-stack-client-python/compare/v0.1.0-alpha.2...v0.1.0-alpha.3)

### Features

* **api:** update via SDK Studio ([e87f225](https://github.com/llamastack/llama-stack-client-python/commit/e87f2257b00a287dd34dc95f4d39661728075891))
* make custom code changes ([#3](https://github.com/llamastack/llama-stack-client-python/issues/3)) ([83fa371](https://github.com/llamastack/llama-stack-client-python/commit/83fa37124133aab73bf2bbbdcd39338b9a192475))

## 0.1.0-alpha.2 (2025-06-27)

Full Changelog: [v0.1.0-alpha.1...v0.1.0-alpha.2](https://github.com/llamastack/llama-stack-client-python/compare/v0.1.0-alpha.1...v0.1.0-alpha.2)

### Features

* **api:** update via SDK Studio ([f568f65](https://github.com/llamastack/llama-stack-client-python/commit/f568f6508002eff7eae4a6b0a1cc13aba6fab98e))

## 0.1.0-alpha.1 (2025-06-27)

Full Changelog: [v0.0.1-alpha.0...v0.1.0-alpha.1](https://github.com/llamastack/llama-stack-client-python/compare/v0.0.1-alpha.0...v0.1.0-alpha.1)

### Features

* **client:** add follow_redirects request option ([a77a9ee](https://github.com/llamastack/llama-stack-client-python/commit/a77a9eed9038782ba6b93ce0d3147ee4a6b8a3b7))
* **client:** add support for aiohttp ([d78982b](https://github.com/llamastack/llama-stack-client-python/commit/d78982b197c5e0a0fb67afcb44e9644fd8d931be))


### Bug Fixes

* **ci:** release-doctor — report correct token name ([6f3a4e2](https://github.com/llamastack/llama-stack-client-python/commit/6f3a4e24d8b357d7dc01adb0d9f736989fa9517d))
* **client:** correctly parse binary response | stream ([85d6bbd](https://github.com/llamastack/llama-stack-client-python/commit/85d6bbd97efac7509cbff0bb2d461a80d09b5e61))
* **package:** support direct resource imports ([a862d55](https://github.com/llamastack/llama-stack-client-python/commit/a862d551553aac41573306ce39480e1eb16ea3d3))
* **tests:** fix: tests which call HTTP endpoints directly with the example parameters ([347a4bf](https://github.com/llamastack/llama-stack-client-python/commit/347a4bffa920f5727a4c02eba18bd207001698b5))


### Chores

* change publish docs url ([fdd7a07](https://github.com/llamastack/llama-stack-client-python/commit/fdd7a075564ac206e91b2d06bf130c4de9473838))
* **ci:** enable for pull requests ([c9b6347](https://github.com/llamastack/llama-stack-client-python/commit/c9b6347f084acb1566b8e8283cf0bcfde7f6562c))
* **ci:** fix installation instructions ([40d9854](https://github.com/llamastack/llama-stack-client-python/commit/40d9854bd2630a471f1ca93d249e4d44b73fa864))
* **ci:** upload sdks to package manager ([2d2282b](https://github.com/llamastack/llama-stack-client-python/commit/2d2282bb49d58daef1f32fa0f1e5a356abf8df0d))
* **docs:** grammar improvements ([6f57b13](https://github.com/llamastack/llama-stack-client-python/commit/6f57b1363367de7ed5035fd1d6ba1a071eee67ba))
* **docs:** remove reference to rye shell ([bcf315a](https://github.com/llamastack/llama-stack-client-python/commit/bcf315ae00c458f89dfa3684bcc7abdb732b6c5f))
* **docs:** remove unnecessary param examples ([60ec829](https://github.com/llamastack/llama-stack-client-python/commit/60ec829e809156217cf2f911b3cac6b23a06baad))
* **internal:** avoid errors for isinstance checks on proxies ([758a188](https://github.com/llamastack/llama-stack-client-python/commit/758a188dbfaa284a13b70816689c99917a05d16c))
* **internal:** codegen related update ([ab9f05c](https://github.com/llamastack/llama-stack-client-python/commit/ab9f05cc1da5b21afceacdf9c8eb54b6e59eed01))
* **internal:** update conftest.py ([218e172](https://github.com/llamastack/llama-stack-client-python/commit/218e172c16014dad41a7c189c5620077955d6bdf))
* **readme:** update badges ([9b63e1b](https://github.com/llamastack/llama-stack-client-python/commit/9b63e1b7dbbbd7556d046a2a4224a8385bbea24c))
* **tests:** add tests for httpx client instantiation & proxies ([b27b11b](https://github.com/llamastack/llama-stack-client-python/commit/b27b11bbe0a9c5778b757733c11828d9603307ea))
* **tests:** run tests in parallel ([1287a3c](https://github.com/llamastack/llama-stack-client-python/commit/1287a3c11f668d916c8c7af534a48523e2e69140))
* **tests:** skip some failing tests on the latest python versions ([73b5705](https://github.com/llamastack/llama-stack-client-python/commit/73b57051c48d2ec42b844a288ffc9b5e3bbe6f2b))
* update SDK settings ([e54ba91](https://github.com/llamastack/llama-stack-client-python/commit/e54ba9163792ab80362a189acb825bcd00e5384b))


### Documentation

* **client:** fix httpx.Timeout documentation reference ([497f2a1](https://github.com/llamastack/llama-stack-client-python/commit/497f2a198140f73525a880497bf1c51b5749c1f3))
