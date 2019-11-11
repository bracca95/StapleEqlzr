###### TAKE A LOOK AT #######
###### https://app.quicktype.io/ #######

# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = preset_from_dict(json.loads(json_string))

from dataclasses import dataclass
from typing import List, Dict, Any, TypeVar, Callable, Type, cast


T = TypeVar("T")


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def from_dict(f: Callable[[Any], T], x: Any) -> Dict[str, T]:
    assert isinstance(x, dict)
    return { k: f(v) for (k, v) in x.items() }


def from_float(x: Any) -> float:
    assert isinstance(x, (float, int)) and not isinstance(x, bool)
    return float(x)


def to_float(x: Any) -> float:
    assert isinstance(x, float)
    return x


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


@dataclass
class Configuration:
    id: int
    name: str
    data: List[Dict[str, float]]

    @staticmethod
    def from_dict(obj: Any) -> 'Configuration':
        assert isinstance(obj, dict)
        id = from_int(obj.get("id"))
        name = from_str(obj.get("name"))
        data = from_list(lambda x: from_dict(from_float, x), obj.get("data"))
        return Configuration(id, name, data)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_int(self.id)
        result["name"] = from_str(self.name)
        result["data"] = from_list(lambda x: from_dict(to_float, x), self.data)
        return result


@dataclass
class Preset:
    version: str
    configurations: List[Configuration]

    @staticmethod
    def from_dict(obj: Any) -> 'Preset':
        assert isinstance(obj, dict)
        version = from_str(obj.get("version"))
        configurations = from_list(Configuration.from_dict, obj.get("configurations"))
        return Preset(version, configurations)

    def to_dict(self) -> dict:
        result: dict = {}
        result["version"] = from_str(self.version)
        result["configurations"] = from_list(lambda x: to_class(Configuration, x), self.configurations)
        return result


def preset_from_dict(s: Any) -> Preset:
    return Preset.from_dict(s)


def preset_to_dict(x: Preset) -> Any:
    return to_class(Preset, x)
