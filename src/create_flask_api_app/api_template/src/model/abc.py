"""Define an Abstract Base Class (ABC) for models."""
import datetime
from weakref import WeakValueDictionary
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy import inspect
from sqlalchemy.orm import aliased


db = SQLAlchemy()


class MetaBaseModel(db.Model.__class__):
    """
        Define a metaclass for the BaseModel to implement `__getitem__` for managing aliases
    """

    def __init__(cls, *args):
        super().__init__(*args)
        cls.aliases = WeakValueDictionary()

    def __getitem__(cls, key):
        try:
            alias = cls.aliases[key]
        except KeyError:
            alias = aliased(cls)
            cls.aliases[key] = alias
        return alias


class BaseModel():
    """
        Generalize __init__, __repr__ and to_json
        Based on the models columns
    """

    print_filter = ()

    def __repr__(self):
        """
            Define a base way to print models
            Columns inside `print_filter` are excluded
        """
        return "{}({})".format(self.__class__.__name__, {
            column: value
            for column, value in self._to_dict().items()
            if column not in self.print_filter
        })

    to_json_filter = ()

    @property
    def json(self):
        """
            Define a base way to jsonify models
            Columns inside `to_json_filter` are excluded
        """
        return {
            column: value if not isinstance(value, datetime.date) else value.isoformat()
            for column, value in self._to_dict().items()
            if column not in self.to_json_filter
        }

    def _to_dict(self):
        """
            This would more or less be the same as a `to_json`
            But putting it in a "private" function
            Allows to_json to be overriden without impacting __repr__
            Or the other way around and to add filter lists
        """
        return {
            column.key: getattr(self, column.key)
            for column in inspect(self.__class__).attrs
        }
