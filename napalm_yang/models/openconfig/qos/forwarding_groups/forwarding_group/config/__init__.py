
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

class config(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-qos - based on the path /qos/forwarding-groups/forwarding-group/config. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Configuration data for forwarding groups
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__name','__fabric_priority','__output_queue',)

  _yang_name = 'config'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__output_queue = YANGDynClass(base=unicode, is_leaf=True, yang_name="output-queue", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/qos', defining_module='openconfig-qos', yang_type='leafref', is_config=True)
    self.__name = YANGDynClass(base=unicode, is_leaf=True, yang_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/qos', defining_module='openconfig-qos', yang_type='string', is_config=True)
    self.__fabric_priority = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="fabric-priority", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/qos', defining_module='openconfig-qos', yang_type='uint8', is_config=True)

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
      return [u'qos', u'forwarding-groups', u'forwarding-group', u'config']

  def _get_name(self):
    """
    Getter method for name, mapped from YANG variable /qos/forwarding_groups/forwarding_group/config/name (string)

    YANG Description: Name of the forwarding group
    """
    return self.__name
      
  def _set_name(self, v, load=False):
    """
    Setter method for name, mapped from YANG variable /qos/forwarding_groups/forwarding_group/config/name (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_name() directly.

    YANG Description: Name of the forwarding group
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/qos', defining_module='openconfig-qos', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """name must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/qos', defining_module='openconfig-qos', yang_type='string', is_config=True)""",
        })

    self.__name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_name(self):
    self.__name = YANGDynClass(base=unicode, is_leaf=True, yang_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/qos', defining_module='openconfig-qos', yang_type='string', is_config=True)


  def _get_fabric_priority(self):
    """
    Getter method for fabric_priority, mapped from YANG variable /qos/forwarding_groups/forwarding_group/config/fabric_priority (uint8)

    YANG Description: Set the priority for the forwarding group for
local transmission through the device, e.g.,
across a switching fabric. Higher priorities
are considered to be better, such that traffic
with fabric priority 128 is considered to be
higher priority than that with fabric priority
0.
    """
    return self.__fabric_priority
      
  def _set_fabric_priority(self, v, load=False):
    """
    Setter method for fabric_priority, mapped from YANG variable /qos/forwarding_groups/forwarding_group/config/fabric_priority (uint8)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_fabric_priority is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_fabric_priority() directly.

    YANG Description: Set the priority for the forwarding group for
local transmission through the device, e.g.,
across a switching fabric. Higher priorities
are considered to be better, such that traffic
with fabric priority 128 is considered to be
higher priority than that with fabric priority
0.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="fabric-priority", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/qos', defining_module='openconfig-qos', yang_type='uint8', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """fabric_priority must be of a type compatible with uint8""",
          'defined-type': "uint8",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="fabric-priority", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/qos', defining_module='openconfig-qos', yang_type='uint8', is_config=True)""",
        })

    self.__fabric_priority = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_fabric_priority(self):
    self.__fabric_priority = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="fabric-priority", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/qos', defining_module='openconfig-qos', yang_type='uint8', is_config=True)


  def _get_output_queue(self):
    """
    Getter method for output_queue, mapped from YANG variable /qos/forwarding_groups/forwarding_group/config/output_queue (leafref)

    YANG Description: Queue for packets in this forwarding group.
    """
    return self.__output_queue
      
  def _set_output_queue(self, v, load=False):
    """
    Setter method for output_queue, mapped from YANG variable /qos/forwarding_groups/forwarding_group/config/output_queue (leafref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_output_queue is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_output_queue() directly.

    YANG Description: Queue for packets in this forwarding group.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="output-queue", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/qos', defining_module='openconfig-qos', yang_type='leafref', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """output_queue must be of a type compatible with leafref""",
          'defined-type': "leafref",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="output-queue", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/qos', defining_module='openconfig-qos', yang_type='leafref', is_config=True)""",
        })

    self.__output_queue = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_output_queue(self):
    self.__output_queue = YANGDynClass(base=unicode, is_leaf=True, yang_name="output-queue", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/qos', defining_module='openconfig-qos', yang_type='leafref', is_config=True)

  name = __builtin__.property(_get_name, _set_name)
  fabric_priority = __builtin__.property(_get_fabric_priority, _set_fabric_priority)
  output_queue = __builtin__.property(_get_output_queue, _set_output_queue)


  _pyangbind_elements = {'name': name, 'fabric_priority': fabric_priority, 'output_queue': output_queue, }


class config(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-qos-interfaces - based on the path /qos/forwarding-groups/forwarding-group/config. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Configuration data for forwarding groups
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__name','__fabric_priority','__output_queue',)

  _yang_name = 'config'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__output_queue = YANGDynClass(base=unicode, is_leaf=True, yang_name="output-queue", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/qos', defining_module='openconfig-qos', yang_type='leafref', is_config=True)
    self.__name = YANGDynClass(base=unicode, is_leaf=True, yang_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/qos', defining_module='openconfig-qos', yang_type='string', is_config=True)
    self.__fabric_priority = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="fabric-priority", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/qos', defining_module='openconfig-qos', yang_type='uint8', is_config=True)

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
      return [u'qos', u'forwarding-groups', u'forwarding-group', u'config']

  def _get_name(self):
    """
    Getter method for name, mapped from YANG variable /qos/forwarding_groups/forwarding_group/config/name (string)

    YANG Description: Name of the forwarding group
    """
    return self.__name
      
  def _set_name(self, v, load=False):
    """
    Setter method for name, mapped from YANG variable /qos/forwarding_groups/forwarding_group/config/name (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_name() directly.

    YANG Description: Name of the forwarding group
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/qos', defining_module='openconfig-qos', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """name must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/qos', defining_module='openconfig-qos', yang_type='string', is_config=True)""",
        })

    self.__name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_name(self):
    self.__name = YANGDynClass(base=unicode, is_leaf=True, yang_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/qos', defining_module='openconfig-qos', yang_type='string', is_config=True)


  def _get_fabric_priority(self):
    """
    Getter method for fabric_priority, mapped from YANG variable /qos/forwarding_groups/forwarding_group/config/fabric_priority (uint8)

    YANG Description: Set the priority for the forwarding group for
local transmission through the device, e.g.,
across a switching fabric. Higher priorities
are considered to be better, such that traffic
with fabric priority 128 is considered to be
higher priority than that with fabric priority
0.
    """
    return self.__fabric_priority
      
  def _set_fabric_priority(self, v, load=False):
    """
    Setter method for fabric_priority, mapped from YANG variable /qos/forwarding_groups/forwarding_group/config/fabric_priority (uint8)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_fabric_priority is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_fabric_priority() directly.

    YANG Description: Set the priority for the forwarding group for
local transmission through the device, e.g.,
across a switching fabric. Higher priorities
are considered to be better, such that traffic
with fabric priority 128 is considered to be
higher priority than that with fabric priority
0.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="fabric-priority", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/qos', defining_module='openconfig-qos', yang_type='uint8', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """fabric_priority must be of a type compatible with uint8""",
          'defined-type': "uint8",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="fabric-priority", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/qos', defining_module='openconfig-qos', yang_type='uint8', is_config=True)""",
        })

    self.__fabric_priority = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_fabric_priority(self):
    self.__fabric_priority = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="fabric-priority", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/qos', defining_module='openconfig-qos', yang_type='uint8', is_config=True)


  def _get_output_queue(self):
    """
    Getter method for output_queue, mapped from YANG variable /qos/forwarding_groups/forwarding_group/config/output_queue (leafref)

    YANG Description: Queue for packets in this forwarding group.
    """
    return self.__output_queue
      
  def _set_output_queue(self, v, load=False):
    """
    Setter method for output_queue, mapped from YANG variable /qos/forwarding_groups/forwarding_group/config/output_queue (leafref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_output_queue is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_output_queue() directly.

    YANG Description: Queue for packets in this forwarding group.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="output-queue", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/qos', defining_module='openconfig-qos', yang_type='leafref', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """output_queue must be of a type compatible with leafref""",
          'defined-type': "leafref",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="output-queue", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/qos', defining_module='openconfig-qos', yang_type='leafref', is_config=True)""",
        })

    self.__output_queue = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_output_queue(self):
    self.__output_queue = YANGDynClass(base=unicode, is_leaf=True, yang_name="output-queue", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/qos', defining_module='openconfig-qos', yang_type='leafref', is_config=True)

  name = __builtin__.property(_get_name, _set_name)
  fabric_priority = __builtin__.property(_get_fabric_priority, _set_fabric_priority)
  output_queue = __builtin__.property(_get_output_queue, _set_output_queue)


  _pyangbind_elements = {'name': name, 'fabric_priority': fabric_priority, 'output_queue': output_queue, }


class config(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-qos-elements - based on the path /qos/forwarding-groups/forwarding-group/config. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Configuration data for forwarding groups
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__name','__fabric_priority','__output_queue',)

  _yang_name = 'config'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__output_queue = YANGDynClass(base=unicode, is_leaf=True, yang_name="output-queue", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/qos', defining_module='openconfig-qos', yang_type='leafref', is_config=True)
    self.__name = YANGDynClass(base=unicode, is_leaf=True, yang_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/qos', defining_module='openconfig-qos', yang_type='string', is_config=True)
    self.__fabric_priority = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="fabric-priority", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/qos', defining_module='openconfig-qos', yang_type='uint8', is_config=True)

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
      return [u'qos', u'forwarding-groups', u'forwarding-group', u'config']

  def _get_name(self):
    """
    Getter method for name, mapped from YANG variable /qos/forwarding_groups/forwarding_group/config/name (string)

    YANG Description: Name of the forwarding group
    """
    return self.__name
      
  def _set_name(self, v, load=False):
    """
    Setter method for name, mapped from YANG variable /qos/forwarding_groups/forwarding_group/config/name (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_name() directly.

    YANG Description: Name of the forwarding group
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/qos', defining_module='openconfig-qos', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """name must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/qos', defining_module='openconfig-qos', yang_type='string', is_config=True)""",
        })

    self.__name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_name(self):
    self.__name = YANGDynClass(base=unicode, is_leaf=True, yang_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/qos', defining_module='openconfig-qos', yang_type='string', is_config=True)


  def _get_fabric_priority(self):
    """
    Getter method for fabric_priority, mapped from YANG variable /qos/forwarding_groups/forwarding_group/config/fabric_priority (uint8)

    YANG Description: Set the priority for the forwarding group for
local transmission through the device, e.g.,
across a switching fabric. Higher priorities
are considered to be better, such that traffic
with fabric priority 128 is considered to be
higher priority than that with fabric priority
0.
    """
    return self.__fabric_priority
      
  def _set_fabric_priority(self, v, load=False):
    """
    Setter method for fabric_priority, mapped from YANG variable /qos/forwarding_groups/forwarding_group/config/fabric_priority (uint8)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_fabric_priority is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_fabric_priority() directly.

    YANG Description: Set the priority for the forwarding group for
local transmission through the device, e.g.,
across a switching fabric. Higher priorities
are considered to be better, such that traffic
with fabric priority 128 is considered to be
higher priority than that with fabric priority
0.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="fabric-priority", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/qos', defining_module='openconfig-qos', yang_type='uint8', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """fabric_priority must be of a type compatible with uint8""",
          'defined-type': "uint8",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="fabric-priority", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/qos', defining_module='openconfig-qos', yang_type='uint8', is_config=True)""",
        })

    self.__fabric_priority = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_fabric_priority(self):
    self.__fabric_priority = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="fabric-priority", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/qos', defining_module='openconfig-qos', yang_type='uint8', is_config=True)


  def _get_output_queue(self):
    """
    Getter method for output_queue, mapped from YANG variable /qos/forwarding_groups/forwarding_group/config/output_queue (leafref)

    YANG Description: Queue for packets in this forwarding group.
    """
    return self.__output_queue
      
  def _set_output_queue(self, v, load=False):
    """
    Setter method for output_queue, mapped from YANG variable /qos/forwarding_groups/forwarding_group/config/output_queue (leafref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_output_queue is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_output_queue() directly.

    YANG Description: Queue for packets in this forwarding group.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="output-queue", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/qos', defining_module='openconfig-qos', yang_type='leafref', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """output_queue must be of a type compatible with leafref""",
          'defined-type': "leafref",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="output-queue", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/qos', defining_module='openconfig-qos', yang_type='leafref', is_config=True)""",
        })

    self.__output_queue = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_output_queue(self):
    self.__output_queue = YANGDynClass(base=unicode, is_leaf=True, yang_name="output-queue", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/qos', defining_module='openconfig-qos', yang_type='leafref', is_config=True)

  name = __builtin__.property(_get_name, _set_name)
  fabric_priority = __builtin__.property(_get_fabric_priority, _set_fabric_priority)
  output_queue = __builtin__.property(_get_output_queue, _set_output_queue)


  _pyangbind_elements = {'name': name, 'fabric_priority': fabric_priority, 'output_queue': output_queue, }


