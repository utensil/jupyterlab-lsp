import json
import pathlib

import jsonschema

HERE = pathlib.Path(__file__).parent
SCHEMA_FILE = HERE / "schema.json"
SCHEMA = json.loads(SCHEMA_FILE.read_text())
SPEC_VERSION = SCHEMA["definitions"]["current-version"]["enum"][0]


def servers_response() -> jsonschema.validators.Draft7Validator:
    """ a validator for the server status API
    """
    return make_validator("servers-response")


def language_server_spec() -> jsonschema.validators.Draft7Validator:
    """ a validator for a language server spec
    """
    return make_validator("language-server-spec")


# utility
def make_validator(key):
    """ make a JSON Schema (Draft 7) validator
    """
    schema = {"$ref": "#/definitions/{}".format(key)}
    schema.update(SCHEMA)
    return jsonschema.validators.Draft7Validator(schema)
