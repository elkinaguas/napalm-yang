
from operator import attrgetter
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType
from pyangbind.lib.yangtypes import RestrictedClassType
from pyangbind.lib.yangtypes import TypedListType
from pyangbind.lib.yangtypes import YANGBool
from pyangbind.lib.yangtypes import YANGListType
from pyangbind.lib.yangtypes import YANGDynClass
from pyangbind.lib.yangtypes import ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import six

# PY3 support of some PY2 keywords (needs improved)
if six.PY3:
  import builtins as __builtin__
  long = int
  unicode = str
elif six.PY2:
  import __builtin__

from . import scheduler
class schedulers(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-qos - based on the path /qos/interfaces/interface/input/scheduler-policy/schedulers. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Schedulers within the applied scheduler-policy.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__scheduler',)

  _yang_name = 'schedulers'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__scheduler = YANGDynClass(base=YANGListType("sequence",scheduler.scheduler, yang_name="scheduler", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='sequence', extensions=None), is_container='list', yang_name="scheduler", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/qos', defining_module='openconfig-qos', yang_type='list', is_config=False)

    load = kwargs.pop("load", None)
    if args:
      if len(args) > 1:
        raise TypeError("cannot create a YANG container with >1 argument")
      all_attr = True
      for e in self._pyangbind_elements:
        if not hasattr(args[0], e):
          all_attr = False
          break
      if not all_attr:
        raise ValueError("Supplied object did not have the correct attributes")
      for e in self._pyangbind_elements:
        nobj = getattr(args[0], e)
        if nobj._changed() is False:
          continue
        setmethod = getattr(self, "_set_%s" % e)
        if load is None:
          setmethod(getattr(args[0], e))
        else:
          setmethod(getattr(args[0], e), load=load)

  def _path(self):
    if hasattr(self, "_parent"):
      return self._parent._path()+[self._yang_name]
    else:
      return [u'qos', u'interfaces', u'interface', u'input', u'scheduler-policy', u'schedulers']

  def _get_scheduler(self):
    """
    Getter method for scheduler, mapped from YANG variable /qos/interfaces/interface/input/scheduler_policy/schedulers/scheduler (list)

    YANG Description: List of the schedulers that are part of the scheduler-policy
specified.
    """
    return self.__scheduler
      
  def _set_scheduler(self, v, load=False):
    """
    Setter method for scheduler, mapped from YANG variable /qos/interfaces/interface/input/scheduler_policy/schedulers/scheduler (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_scheduler is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_scheduler() directly.

    YANG Description: List of the schedulers that are part of the scheduler-policy
specified.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("sequence",scheduler.scheduler, yang_name="scheduler", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='sequence', extensions=None), is_container='list', yang_name="scheduler", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/qos', defining_module='openconfig-qos', yang_type='list', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """scheduler must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("sequence",scheduler.scheduler, yang_name="scheduler", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='sequence', extensions=None), is_container='list', yang_name="scheduler", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/qos', defining_module='openconfig-qos', yang_type='list', is_config=False)""",
        })

    self.__scheduler = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_scheduler(self):
    self.__scheduler = YANGDynClass(base=YANGListType("sequence",scheduler.scheduler, yang_name="scheduler", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='sequence', extensions=None), is_container='list', yang_name="scheduler", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/qos', defining_module='openconfig-qos', yang_type='list', is_config=False)

  scheduler = __builtin__.property(_get_scheduler)


  _pyangbind_elements = {'scheduler': scheduler, }


from . import scheduler
class schedulers(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-qos-interfaces - based on the path /qos/interfaces/interface/input/scheduler-policy/schedulers. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Schedulers within the applied scheduler-policy.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__scheduler',)

  _yang_name = 'schedulers'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__scheduler = YANGDynClass(base=YANGListType("sequence",scheduler.scheduler, yang_name="scheduler", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='sequence', extensions=None), is_container='list', yang_name="scheduler", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/qos', defining_module='openconfig-qos', yang_type='list', is_config=False)

    load = kwargs.pop("load", None)
    if args:
      if len(args) > 1:
        raise TypeError("cannot create a YANG container with >1 argument")
      all_attr = True
      for e in self._pyangbind_elements:
        if not hasattr(args[0], e):
          all_attr = False
          break
      if not all_attr:
        raise ValueError("Supplied object did not have the correct attributes")
      for e in self._pyangbind_elements:
        nobj = getattr(args[0], e)
        if nobj._changed() is False:
          continue
        setmethod = getattr(self, "_set_%s" % e)
        if load is None:
          setmethod(getattr(args[0], e))
        else:
          setmethod(getattr(args[0], e), load=load)

  def _path(self):
    if hasattr(self, "_parent"):
      return self._parent._path()+[self._yang_name]
    else:
      return [u'qos', u'interfaces', u'interface', u'input', u'scheduler-policy', u'schedulers']

  def _get_scheduler(self):
    """
    Getter method for scheduler, mapped from YANG variable /qos/interfaces/interface/input/scheduler_policy/schedulers/scheduler (list)

    YANG Description: List of the schedulers that are part of the scheduler-policy
specified.
    """
    return self.__scheduler
      
  def _set_scheduler(self, v, load=False):
    """
    Setter method for scheduler, mapped from YANG variable /qos/interfaces/interface/input/scheduler_policy/schedulers/scheduler (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_scheduler is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_scheduler() directly.

    YANG Description: List of the schedulers that are part of the scheduler-policy
specified.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("sequence",scheduler.scheduler, yang_name="scheduler", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='sequence', extensions=None), is_container='list', yang_name="scheduler", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/qos', defining_module='openconfig-qos', yang_type='list', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """scheduler must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("sequence",scheduler.scheduler, yang_name="scheduler", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='sequence', extensions=None), is_container='list', yang_name="scheduler", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/qos', defining_module='openconfig-qos', yang_type='list', is_config=False)""",
        })

    self.__scheduler = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_scheduler(self):
    self.__scheduler = YANGDynClass(base=YANGListType("sequence",scheduler.scheduler, yang_name="scheduler", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='sequence', extensions=None), is_container='list', yang_name="scheduler", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/qos', defining_module='openconfig-qos', yang_type='list', is_config=False)

  scheduler = __builtin__.property(_get_scheduler)


  _pyangbind_elements = {'scheduler': scheduler, }


from . import scheduler
class schedulers(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-qos-elements - based on the path /qos/interfaces/interface/input/scheduler-policy/schedulers. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Schedulers within the applied scheduler-policy.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__scheduler',)

  _yang_name = 'schedulers'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__scheduler = YANGDynClass(base=YANGListType("sequence",scheduler.scheduler, yang_name="scheduler", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='sequence', extensions=None), is_container='list', yang_name="scheduler", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/qos', defining_module='openconfig-qos', yang_type='list', is_config=False)

    load = kwargs.pop("load", None)
    if args:
      if len(args) > 1:
        raise TypeError("cannot create a YANG container with >1 argument")
      all_attr = True
      for e in self._pyangbind_elements:
        if not hasattr(args[0], e):
          all_attr = False
          break
      if not all_attr:
        raise ValueError("Supplied object did not have the correct attributes")
      for e in self._pyangbind_elements:
        nobj = getattr(args[0], e)
        if nobj._changed() is False:
          continue
        setmethod = getattr(self, "_set_%s" % e)
        if load is None:
          setmethod(getattr(args[0], e))
        else:
          setmethod(getattr(args[0], e), load=load)

  def _path(self):
    if hasattr(self, "_parent"):
      return self._parent._path()+[self._yang_name]
    else:
      return [u'qos', u'interfaces', u'interface', u'input', u'scheduler-policy', u'schedulers']

  def _get_scheduler(self):
    """
    Getter method for scheduler, mapped from YANG variable /qos/interfaces/interface/input/scheduler_policy/schedulers/scheduler (list)

    YANG Description: List of the schedulers that are part of the scheduler-policy
specified.
    """
    return self.__scheduler
      
  def _set_scheduler(self, v, load=False):
    """
    Setter method for scheduler, mapped from YANG variable /qos/interfaces/interface/input/scheduler_policy/schedulers/scheduler (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_scheduler is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_scheduler() directly.

    YANG Description: List of the schedulers that are part of the scheduler-policy
specified.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("sequence",scheduler.scheduler, yang_name="scheduler", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='sequence', extensions=None), is_container='list', yang_name="scheduler", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/qos', defining_module='openconfig-qos', yang_type='list', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """scheduler must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("sequence",scheduler.scheduler, yang_name="scheduler", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='sequence', extensions=None), is_container='list', yang_name="scheduler", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/qos', defining_module='openconfig-qos', yang_type='list', is_config=False)""",
        })

    self.__scheduler = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_scheduler(self):
    self.__scheduler = YANGDynClass(base=YANGListType("sequence",scheduler.scheduler, yang_name="scheduler", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='sequence', extensions=None), is_container='list', yang_name="scheduler", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/qos', defining_module='openconfig-qos', yang_type='list', is_config=False)

  scheduler = __builtin__.property(_get_scheduler)


  _pyangbind_elements = {'scheduler': scheduler, }


