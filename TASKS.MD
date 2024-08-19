# Tasks

- [x]  Install dependencies
    - [x]  Resolve problem when try to run project
        - Some problem happend
            
            ```python
            Traceback (most recent call last):
              File "/usr/lib/python3.10/multiprocessing/process.py", line 314, in _bootstrap
                self.run()
              File "/usr/lib/python3.10/multiprocessing/process.py", line 108, in run
                self._target(*self._args, **self._kwargs)
              File "/home/sesplnl79955/.local/lib/python3.10/site-packages/uvicorn/_subprocess.py", line 80, in subprocess_started
                target(sockets=sockets)
              File "/home/sesplnl79955/.local/lib/python3.10/site-packages/uvicorn/server.py", line 65, in run
                return asyncio.run(self.serve(sockets=sockets))
              File "/usr/lib/python3.10/asyncio/runners.py", line 44, in run
                return loop.run_until_complete(main)
              File "/usr/lib/python3.10/asyncio/base_events.py", line 649, in run_until_complete
                return future.result()
              File "/home/sesplnl79955/.local/lib/python3.10/site-packages/uvicorn/server.py", line 69, in serve
                await self._serve(sockets)
              File "/home/sesplnl79955/.local/lib/python3.10/site-packages/uvicorn/server.py", line 76, in _serve
                config.load()
              File "/home/sesplnl79955/.local/lib/python3.10/site-packages/uvicorn/config.py", line 434, in load
                self.loaded_app = import_from_string(self.app)
              File "/home/sesplnl79955/.local/lib/python3.10/site-packages/uvicorn/importer.py", line 19, in import_from_string
                module = importlib.import_module(module_str)
              File "/usr/lib/python3.10/importlib/__init__.py", line 126, in import_module
                return _bootstrap._gcd_import(name[level:], package, level)
              File "<frozen importlib._bootstrap>", line 1050, in _gcd_import
              File "<frozen importlib._bootstrap>", line 1027, in _find_and_load
              File "<frozen importlib._bootstrap>", line 1006, in _find_and_load_unlocked
              File "<frozen importlib._bootstrap>", line 688, in _load_unlocked
              File "<frozen importlib._bootstrap_external>", line 883, in exec_module
              File "<frozen importlib._bootstrap>", line 241, in _call_with_frames_removed
              File "/home/sesplnl79955/test_interview/api_todo/main.py", line 1, in <module>
                from fastapi import FastAPI, Request
              File "/home/sesplnl79955/.local/lib/python3.10/site-packages/fastapi/__init__.py", line 7, in <module>
                from .applications import FastAPI as FastAPI
              File "/home/sesplnl79955/.local/lib/python3.10/site-packages/fastapi/applications.py", line 16, in <module>
                from fastapi import routing
              File "/home/sesplnl79955/.local/lib/python3.10/site-packages/fastapi/routing.py", line 22, in <module>
                from fastapi import params
              File "/home/sesplnl79955/.local/lib/python3.10/site-packages/fastapi/params.py", line 5, in <module>
                from fastapi.openapi.models import Example
              File "/home/sesplnl79955/.local/lib/python3.10/site-packages/fastapi/openapi/models.py", line 68, in <module>
                class Contact(BaseModelWithConfig):
              File "/home/sesplnl79955/.local/lib/python3.10/site-packages/pydantic/_internal/_model_construction.py", line 205, in __new__
                complete_model_class(
              File "/home/sesplnl79955/.local/lib/python3.10/site-packages/pydantic/_internal/_model_construction.py", line 534, in complete_model_class
                schema = cls.__get_pydantic_core_schema__(cls, handler)
              File "/home/sesplnl79955/.local/lib/python3.10/site-packages/pydantic/main.py", line 643, in __get_pydantic_core_schema__
                return handler(source)
              File "/home/sesplnl79955/.local/lib/python3.10/site-packages/pydantic/_internal/_schema_generation_shared.py", line 83, in __call__
                schema = self._handler(source_type)
              File "/home/sesplnl79955/.local/lib/python3.10/site-packages/pydantic/_internal/_generate_schema.py", line 512, in generate_schema
                schema = self._generate_schema_inner(obj)
              File "/home/sesplnl79955/.local/lib/python3.10/site-packages/pydantic/_internal/_generate_schema.py", line 784, in _generate_schema_inner
                return self._model_schema(obj)
              File "/home/sesplnl79955/.local/lib/python3.10/site-packages/pydantic/_internal/_generate_schema.py", line 591, in _model_schema
                {k: self._generate_md_field_schema(k, v, decorators) for k, v in fields.items()},
              File "/home/sesplnl79955/.local/lib/python3.10/site-packages/pydantic/_internal/_generate_schema.py", line 591, in <dictcomp>
                {k: self._generate_md_field_schema(k, v, decorators) for k, v in fields.items()},
              File "/home/sesplnl79955/.local/lib/python3.10/site-packages/pydantic/_internal/_generate_schema.py", line 947, in _generate_md_field_schema
                common_field = self._common_field_schema(name, field_info, decorators)
              File "/home/sesplnl79955/.local/lib/python3.10/site-packages/pydantic/_internal/_generate_schema.py", line 1134, in _common_field_schema
                schema = self._apply_annotations(
              File "/home/sesplnl79955/.local/lib/python3.10/site-packages/pydantic/_internal/_generate_schema.py", line 1890, in _apply_annotations
                schema = get_inner_schema(source_type)
              File "/home/sesplnl79955/.local/lib/python3.10/site-packages/pydantic/_internal/_schema_generation_shared.py", line 83, in __call__
                schema = self._handler(source_type)
              File "/home/sesplnl79955/.local/lib/python3.10/site-packages/pydantic/_internal/_generate_schema.py", line 1871, in inner_handler
                schema = self._generate_schema_inner(obj)
              File "/home/sesplnl79955/.local/lib/python3.10/site-packages/pydantic/_internal/_generate_schema.py", line 789, in _generate_schema_inner
                return self.match_type(obj)
              File "/home/sesplnl79955/.local/lib/python3.10/site-packages/pydantic/_internal/_generate_schema.py", line 871, in match_type
                return self._match_generic_type(obj, origin)
              File "/home/sesplnl79955/.local/lib/python3.10/site-packages/pydantic/_internal/_generate_schema.py", line 895, in _match_generic_type
                return self._union_schema(obj)
              File "/home/sesplnl79955/.local/lib/python3.10/site-packages/pydantic/_internal/_generate_schema.py", line 1207, in _union_schema
                choices.append(self.generate_schema(arg))
              File "/home/sesplnl79955/.local/lib/python3.10/site-packages/pydantic/_internal/_generate_schema.py", line 507, in generate_schema
                from_property = self._generate_schema_from_property(obj, obj)
              File "/home/sesplnl79955/.local/lib/python3.10/site-packages/pydantic/_internal/_generate_schema.py", line 679, in _generate_schema_from_property
                schema = get_schema(
              File "/home/sesplnl79955/.local/lib/python3.10/site-packages/pydantic/networks.py", line 444, in __get_pydantic_core_schema__
                import_email_validator()
              File "/home/sesplnl79955/.local/lib/python3.10/site-packages/pydantic/networks.py", line 408, in import_email_validator
                raise ImportError('email-validator version >= 2.0 required, run pip install -U email-validator')
            ImportError: email-validator version >= 2.0 required, run pip install -U email-validator
            ```
            
        
        I add in requirements.txt and the problem was fixed
        
        ```
        email-validator>=2.0
        ```
        
- [x]  Add a new Endpoint to migrate data
    - [x]  Create function to Migrate Data
        - [x]  Read Json File
        - [x]  Put Object in MongoDB
        - [x]  Transform object in appropriate format
        - [x]  Ensure proper error handling during the migration process.
        - [x]  change the way the project handles numeric values. to add +1 to the last record delivered
    - [x]  Create endpoint to migrate Data
        - [x]  Insert the logic in endpoint
        - [x]  Ensure proper error handling during the migration process.
- [x]  Modify Existing Endpoints
    - [x]  Refactor the data layer to use MongoDB instead of the existing data storage method.
    - [x]  Ensure proper error handling during the migration process.
    - [x]  improve function names
- [x]  Refactor todolist.html to Run with new contract of the data
    - [x]  Create migration button
- [x]  Refactor numeric management to avoid conflicts with add, delete and migrate operations
- [x]  Refactoring the project structure
  - [x] Break main.py into modules
    - [x] Create routing module
    - [x] Create  module with project logic (service)
    - [x] Create  module for connecting to third party resources (db)
    - [x] Create  module for loading configuration into the project
    - [x] Create module for code reuse (common)
- [x]  Create Docker file to create API image
- [x]  Add API image in Docker compose


ROADMAP
- [] Create integration tests to ensure E2E functionality
- [] Create unit tests for common utils and features in todo_service