#!/usr/bin/python3
"""This is the base model."""

from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """The initialization method of attributes"""

    def __init__(self, *args, **kwargs):
        Date_time_format = "%Y-%m-%dT%H:%M:%S.%f"
        if kwargs:
            for ky, val in kwargs.items():
                if ky == "__class__":
                    continue
                elif ky == "created_at" or ky == "updated_at":
                    val = datetime.strptime(val, Date_time_format)
                else:
                    setattr(self, ky, val)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """__str__.
        Return string representation.
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Save.
        Update updated_at with the current datetime.
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Return the dictionary containing key-value pairs.
        """
        dic_res = self.__dict__.copy()
        dic_res["__class__"] = self.__class__.__name__
        dic_res["created_at"] = self.created_at.isoformat()
        dic_res["updated_at"] = self.updated_at.isoformat()
        return dic_res
