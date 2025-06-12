# -*- coding: utf-8 -*-
from abc import abstractmethod

from qudi.core.module import Base


class NvTestPulserInterface(Base):
    """ This is a simple template hardware interface for qudi.
    """
    @property
    @abstractmethod
    def trigger_time(self) -> float:
        """ Read-only property holding the trigger high duration.
        """
        pass

    @abstractmethod
    def send_trigger(self) -> None:
        """ Send a single trigger.
        """
        pass