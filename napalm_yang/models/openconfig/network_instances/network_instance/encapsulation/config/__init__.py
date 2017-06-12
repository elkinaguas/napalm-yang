
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
import __builtin__
import six

# PY3 support of some PY2 keywords (needs improved)
if six.PY3:
 long = int
 unicode = str

class config(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/encapsulation/config. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Configuration parameters relating to the encapsulation
of the network instance
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__encapsulation_type','__label_allocation_mode','__control_word',)

  _yang_name = 'config'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__encapsulation_type = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_type="dict_key", restriction_arg={u'oc-ni-types:VXLAN': {'@namespace': u'http://openconfig.net/yang/network-instance-types', '@module': u'openconfig-network-instance-types'}, u'oc-ni-types:MPLS': {'@namespace': u'http://openconfig.net/yang/network-instance-types', '@module': u'openconfig-network-instance-types'}, u'MPLS': {'@namespace': u'http://openconfig.net/yang/network-instance-types', '@module': u'openconfig-network-instance-types'}, u'VXLAN': {'@namespace': u'http://openconfig.net/yang/network-instance-types', '@module': u'openconfig-network-instance-types'}},), is_leaf=True, yang_name="encapsulation-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='identityref', is_config=True)
    self.__label_allocation_mode = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_type="dict_key", restriction_arg={u'INSTANCE_LABEL': {'@namespace': u'http://openconfig.net/yang/network-instance-types', '@module': u'openconfig-network-instance-types'}, u'oc-ni-types:PER_NEXTHOP': {'@namespace': u'http://openconfig.net/yang/network-instance-types', '@module': u'openconfig-network-instance-types'}, u'PER_PREFIX': {'@namespace': u'http://openconfig.net/yang/network-instance-types', '@module': u'openconfig-network-instance-types'}, u'oc-ni-types:INSTANCE_LABEL': {'@namespace': u'http://openconfig.net/yang/network-instance-types', '@module': u'openconfig-network-instance-types'}, u'oc-ni-types:PER_PREFIX': {'@namespace': u'http://openconfig.net/yang/network-instance-types', '@module': u'openconfig-network-instance-types'}, u'PER_NEXTHOP': {'@namespace': u'http://openconfig.net/yang/network-instance-types', '@module': u'openconfig-network-instance-types'}},), is_leaf=True, yang_name="label-allocation-mode", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='identityref', is_config=True)
    self.__control_word = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="control-word", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)

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
      return [u'network-instances', u'network-instance', u'encapsulation', u'config']

  def _get_encapsulation_type(self):
    """
    Getter method for encapsulation_type, mapped from YANG variable /network_instances/network_instance/encapsulation/config/encapsulation_type (identityref)

    YANG Description: The on-the-wire encapsulation that should be used when
sending traffic from this network instance
    """
    return self.__encapsulation_type
      
  def _set_encapsulation_type(self, v, load=False):
    """
    Setter method for encapsulation_type, mapped from YANG variable /network_instances/network_instance/encapsulation/config/encapsulation_type (identityref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_encapsulation_type is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_encapsulation_type() directly.

    YANG Description: The on-the-wire encapsulation that should be used when
sending traffic from this network instance
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_type="dict_key", restriction_arg={u'oc-ni-types:VXLAN': {'@namespace': u'http://openconfig.net/yang/network-instance-types', '@module': u'openconfig-network-instance-types'}, u'oc-ni-types:MPLS': {'@namespace': u'http://openconfig.net/yang/network-instance-types', '@module': u'openconfig-network-instance-types'}, u'MPLS': {'@namespace': u'http://openconfig.net/yang/network-instance-types', '@module': u'openconfig-network-instance-types'}, u'VXLAN': {'@namespace': u'http://openconfig.net/yang/network-instance-types', '@module': u'openconfig-network-instance-types'}},), is_leaf=True, yang_name="encapsulation-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='identityref', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """encapsulation_type must be of a type compatible with identityref""",
          'defined-type': "openconfig-network-instance:identityref",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_type="dict_key", restriction_arg={u'oc-ni-types:VXLAN': {'@namespace': u'http://openconfig.net/yang/network-instance-types', '@module': u'openconfig-network-instance-types'}, u'oc-ni-types:MPLS': {'@namespace': u'http://openconfig.net/yang/network-instance-types', '@module': u'openconfig-network-instance-types'}, u'MPLS': {'@namespace': u'http://openconfig.net/yang/network-instance-types', '@module': u'openconfig-network-instance-types'}, u'VXLAN': {'@namespace': u'http://openconfig.net/yang/network-instance-types', '@module': u'openconfig-network-instance-types'}},), is_leaf=True, yang_name="encapsulation-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='identityref', is_config=True)""",
        })

    self.__encapsulation_type = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_encapsulation_type(self):
    self.__encapsulation_type = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_type="dict_key", restriction_arg={u'oc-ni-types:VXLAN': {'@namespace': u'http://openconfig.net/yang/network-instance-types', '@module': u'openconfig-network-instance-types'}, u'oc-ni-types:MPLS': {'@namespace': u'http://openconfig.net/yang/network-instance-types', '@module': u'openconfig-network-instance-types'}, u'MPLS': {'@namespace': u'http://openconfig.net/yang/network-instance-types', '@module': u'openconfig-network-instance-types'}, u'VXLAN': {'@namespace': u'http://openconfig.net/yang/network-instance-types', '@module': u'openconfig-network-instance-types'}},), is_leaf=True, yang_name="encapsulation-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='identityref', is_config=True)


  def _get_label_allocation_mode(self):
    """
    Getter method for label_allocation_mode, mapped from YANG variable /network_instances/network_instance/encapsulation/config/label_allocation_mode (identityref)

    YANG Description: The label allocation mode to be used for L3 entries
in the network instance
    """
    return self.__label_allocation_mode
      
  def _set_label_allocation_mode(self, v, load=False):
    """
    Setter method for label_allocation_mode, mapped from YANG variable /network_instances/network_instance/encapsulation/config/label_allocation_mode (identityref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_label_allocation_mode is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_label_allocation_mode() directly.

    YANG Description: The label allocation mode to be used for L3 entries
in the network instance
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_type="dict_key", restriction_arg={u'INSTANCE_LABEL': {'@namespace': u'http://openconfig.net/yang/network-instance-types', '@module': u'openconfig-network-instance-types'}, u'oc-ni-types:PER_NEXTHOP': {'@namespace': u'http://openconfig.net/yang/network-instance-types', '@module': u'openconfig-network-instance-types'}, u'PER_PREFIX': {'@namespace': u'http://openconfig.net/yang/network-instance-types', '@module': u'openconfig-network-instance-types'}, u'oc-ni-types:INSTANCE_LABEL': {'@namespace': u'http://openconfig.net/yang/network-instance-types', '@module': u'openconfig-network-instance-types'}, u'oc-ni-types:PER_PREFIX': {'@namespace': u'http://openconfig.net/yang/network-instance-types', '@module': u'openconfig-network-instance-types'}, u'PER_NEXTHOP': {'@namespace': u'http://openconfig.net/yang/network-instance-types', '@module': u'openconfig-network-instance-types'}},), is_leaf=True, yang_name="label-allocation-mode", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='identityref', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """label_allocation_mode must be of a type compatible with identityref""",
          'defined-type': "openconfig-network-instance:identityref",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_type="dict_key", restriction_arg={u'INSTANCE_LABEL': {'@namespace': u'http://openconfig.net/yang/network-instance-types', '@module': u'openconfig-network-instance-types'}, u'oc-ni-types:PER_NEXTHOP': {'@namespace': u'http://openconfig.net/yang/network-instance-types', '@module': u'openconfig-network-instance-types'}, u'PER_PREFIX': {'@namespace': u'http://openconfig.net/yang/network-instance-types', '@module': u'openconfig-network-instance-types'}, u'oc-ni-types:INSTANCE_LABEL': {'@namespace': u'http://openconfig.net/yang/network-instance-types', '@module': u'openconfig-network-instance-types'}, u'oc-ni-types:PER_PREFIX': {'@namespace': u'http://openconfig.net/yang/network-instance-types', '@module': u'openconfig-network-instance-types'}, u'PER_NEXTHOP': {'@namespace': u'http://openconfig.net/yang/network-instance-types', '@module': u'openconfig-network-instance-types'}},), is_leaf=True, yang_name="label-allocation-mode", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='identityref', is_config=True)""",
        })

    self.__label_allocation_mode = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_label_allocation_mode(self):
    self.__label_allocation_mode = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_type="dict_key", restriction_arg={u'INSTANCE_LABEL': {'@namespace': u'http://openconfig.net/yang/network-instance-types', '@module': u'openconfig-network-instance-types'}, u'oc-ni-types:PER_NEXTHOP': {'@namespace': u'http://openconfig.net/yang/network-instance-types', '@module': u'openconfig-network-instance-types'}, u'PER_PREFIX': {'@namespace': u'http://openconfig.net/yang/network-instance-types', '@module': u'openconfig-network-instance-types'}, u'oc-ni-types:INSTANCE_LABEL': {'@namespace': u'http://openconfig.net/yang/network-instance-types', '@module': u'openconfig-network-instance-types'}, u'oc-ni-types:PER_PREFIX': {'@namespace': u'http://openconfig.net/yang/network-instance-types', '@module': u'openconfig-network-instance-types'}, u'PER_NEXTHOP': {'@namespace': u'http://openconfig.net/yang/network-instance-types', '@module': u'openconfig-network-instance-types'}},), is_leaf=True, yang_name="label-allocation-mode", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='identityref', is_config=True)


  def _get_control_word(self):
    """
    Getter method for control_word, mapped from YANG variable /network_instances/network_instance/encapsulation/config/control_word (boolean)

    YANG Description: Whether the control-word should be used for the network
instance
    """
    return self.__control_word
      
  def _set_control_word(self, v, load=False):
    """
    Setter method for control_word, mapped from YANG variable /network_instances/network_instance/encapsulation/config/control_word (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_control_word is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_control_word() directly.

    YANG Description: Whether the control-word should be used for the network
instance
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="control-word", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """control_word must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="control-word", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)""",
        })

    self.__control_word = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_control_word(self):
    self.__control_word = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="control-word", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)

  encapsulation_type = __builtin__.property(_get_encapsulation_type, _set_encapsulation_type)
  label_allocation_mode = __builtin__.property(_get_label_allocation_mode, _set_label_allocation_mode)
  control_word = __builtin__.property(_get_control_word, _set_control_word)


  _pyangbind_elements = {'encapsulation_type': encapsulation_type, 'label_allocation_mode': label_allocation_mode, 'control_word': control_word, }


class config(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/encapsulation/config. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Configuration parameters relating to the encapsulation
of the network instance
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__encapsulation_type','__label_allocation_mode','__control_word',)

  _yang_name = 'config'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__encapsulation_type = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_type="dict_key", restriction_arg={u'oc-ni-types:VXLAN': {'@namespace': u'http://openconfig.net/yang/network-instance-types', '@module': u'openconfig-network-instance-types'}, u'oc-ni-types:MPLS': {'@namespace': u'http://openconfig.net/yang/network-instance-types', '@module': u'openconfig-network-instance-types'}, u'MPLS': {'@namespace': u'http://openconfig.net/yang/network-instance-types', '@module': u'openconfig-network-instance-types'}, u'VXLAN': {'@namespace': u'http://openconfig.net/yang/network-instance-types', '@module': u'openconfig-network-instance-types'}},), is_leaf=True, yang_name="encapsulation-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='identityref', is_config=True)
    self.__label_allocation_mode = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_type="dict_key", restriction_arg={u'INSTANCE_LABEL': {'@namespace': u'http://openconfig.net/yang/network-instance-types', '@module': u'openconfig-network-instance-types'}, u'oc-ni-types:PER_NEXTHOP': {'@namespace': u'http://openconfig.net/yang/network-instance-types', '@module': u'openconfig-network-instance-types'}, u'PER_PREFIX': {'@namespace': u'http://openconfig.net/yang/network-instance-types', '@module': u'openconfig-network-instance-types'}, u'oc-ni-types:INSTANCE_LABEL': {'@namespace': u'http://openconfig.net/yang/network-instance-types', '@module': u'openconfig-network-instance-types'}, u'oc-ni-types:PER_PREFIX': {'@namespace': u'http://openconfig.net/yang/network-instance-types', '@module': u'openconfig-network-instance-types'}, u'PER_NEXTHOP': {'@namespace': u'http://openconfig.net/yang/network-instance-types', '@module': u'openconfig-network-instance-types'}},), is_leaf=True, yang_name="label-allocation-mode", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='identityref', is_config=True)
    self.__control_word = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="control-word", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)

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
      return [u'network-instances', u'network-instance', u'encapsulation', u'config']

  def _get_encapsulation_type(self):
    """
    Getter method for encapsulation_type, mapped from YANG variable /network_instances/network_instance/encapsulation/config/encapsulation_type (identityref)

    YANG Description: The on-the-wire encapsulation that should be used when
sending traffic from this network instance
    """
    return self.__encapsulation_type
      
  def _set_encapsulation_type(self, v, load=False):
    """
    Setter method for encapsulation_type, mapped from YANG variable /network_instances/network_instance/encapsulation/config/encapsulation_type (identityref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_encapsulation_type is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_encapsulation_type() directly.

    YANG Description: The on-the-wire encapsulation that should be used when
sending traffic from this network instance
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_type="dict_key", restriction_arg={u'oc-ni-types:VXLAN': {'@namespace': u'http://openconfig.net/yang/network-instance-types', '@module': u'openconfig-network-instance-types'}, u'oc-ni-types:MPLS': {'@namespace': u'http://openconfig.net/yang/network-instance-types', '@module': u'openconfig-network-instance-types'}, u'MPLS': {'@namespace': u'http://openconfig.net/yang/network-instance-types', '@module': u'openconfig-network-instance-types'}, u'VXLAN': {'@namespace': u'http://openconfig.net/yang/network-instance-types', '@module': u'openconfig-network-instance-types'}},), is_leaf=True, yang_name="encapsulation-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='identityref', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """encapsulation_type must be of a type compatible with identityref""",
          'defined-type': "openconfig-network-instance:identityref",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_type="dict_key", restriction_arg={u'oc-ni-types:VXLAN': {'@namespace': u'http://openconfig.net/yang/network-instance-types', '@module': u'openconfig-network-instance-types'}, u'oc-ni-types:MPLS': {'@namespace': u'http://openconfig.net/yang/network-instance-types', '@module': u'openconfig-network-instance-types'}, u'MPLS': {'@namespace': u'http://openconfig.net/yang/network-instance-types', '@module': u'openconfig-network-instance-types'}, u'VXLAN': {'@namespace': u'http://openconfig.net/yang/network-instance-types', '@module': u'openconfig-network-instance-types'}},), is_leaf=True, yang_name="encapsulation-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='identityref', is_config=True)""",
        })

    self.__encapsulation_type = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_encapsulation_type(self):
    self.__encapsulation_type = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_type="dict_key", restriction_arg={u'oc-ni-types:VXLAN': {'@namespace': u'http://openconfig.net/yang/network-instance-types', '@module': u'openconfig-network-instance-types'}, u'oc-ni-types:MPLS': {'@namespace': u'http://openconfig.net/yang/network-instance-types', '@module': u'openconfig-network-instance-types'}, u'MPLS': {'@namespace': u'http://openconfig.net/yang/network-instance-types', '@module': u'openconfig-network-instance-types'}, u'VXLAN': {'@namespace': u'http://openconfig.net/yang/network-instance-types', '@module': u'openconfig-network-instance-types'}},), is_leaf=True, yang_name="encapsulation-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='identityref', is_config=True)


  def _get_label_allocation_mode(self):
    """
    Getter method for label_allocation_mode, mapped from YANG variable /network_instances/network_instance/encapsulation/config/label_allocation_mode (identityref)

    YANG Description: The label allocation mode to be used for L3 entries
in the network instance
    """
    return self.__label_allocation_mode
      
  def _set_label_allocation_mode(self, v, load=False):
    """
    Setter method for label_allocation_mode, mapped from YANG variable /network_instances/network_instance/encapsulation/config/label_allocation_mode (identityref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_label_allocation_mode is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_label_allocation_mode() directly.

    YANG Description: The label allocation mode to be used for L3 entries
in the network instance
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_type="dict_key", restriction_arg={u'INSTANCE_LABEL': {'@namespace': u'http://openconfig.net/yang/network-instance-types', '@module': u'openconfig-network-instance-types'}, u'oc-ni-types:PER_NEXTHOP': {'@namespace': u'http://openconfig.net/yang/network-instance-types', '@module': u'openconfig-network-instance-types'}, u'PER_PREFIX': {'@namespace': u'http://openconfig.net/yang/network-instance-types', '@module': u'openconfig-network-instance-types'}, u'oc-ni-types:INSTANCE_LABEL': {'@namespace': u'http://openconfig.net/yang/network-instance-types', '@module': u'openconfig-network-instance-types'}, u'oc-ni-types:PER_PREFIX': {'@namespace': u'http://openconfig.net/yang/network-instance-types', '@module': u'openconfig-network-instance-types'}, u'PER_NEXTHOP': {'@namespace': u'http://openconfig.net/yang/network-instance-types', '@module': u'openconfig-network-instance-types'}},), is_leaf=True, yang_name="label-allocation-mode", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='identityref', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """label_allocation_mode must be of a type compatible with identityref""",
          'defined-type': "openconfig-network-instance:identityref",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_type="dict_key", restriction_arg={u'INSTANCE_LABEL': {'@namespace': u'http://openconfig.net/yang/network-instance-types', '@module': u'openconfig-network-instance-types'}, u'oc-ni-types:PER_NEXTHOP': {'@namespace': u'http://openconfig.net/yang/network-instance-types', '@module': u'openconfig-network-instance-types'}, u'PER_PREFIX': {'@namespace': u'http://openconfig.net/yang/network-instance-types', '@module': u'openconfig-network-instance-types'}, u'oc-ni-types:INSTANCE_LABEL': {'@namespace': u'http://openconfig.net/yang/network-instance-types', '@module': u'openconfig-network-instance-types'}, u'oc-ni-types:PER_PREFIX': {'@namespace': u'http://openconfig.net/yang/network-instance-types', '@module': u'openconfig-network-instance-types'}, u'PER_NEXTHOP': {'@namespace': u'http://openconfig.net/yang/network-instance-types', '@module': u'openconfig-network-instance-types'}},), is_leaf=True, yang_name="label-allocation-mode", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='identityref', is_config=True)""",
        })

    self.__label_allocation_mode = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_label_allocation_mode(self):
    self.__label_allocation_mode = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_type="dict_key", restriction_arg={u'INSTANCE_LABEL': {'@namespace': u'http://openconfig.net/yang/network-instance-types', '@module': u'openconfig-network-instance-types'}, u'oc-ni-types:PER_NEXTHOP': {'@namespace': u'http://openconfig.net/yang/network-instance-types', '@module': u'openconfig-network-instance-types'}, u'PER_PREFIX': {'@namespace': u'http://openconfig.net/yang/network-instance-types', '@module': u'openconfig-network-instance-types'}, u'oc-ni-types:INSTANCE_LABEL': {'@namespace': u'http://openconfig.net/yang/network-instance-types', '@module': u'openconfig-network-instance-types'}, u'oc-ni-types:PER_PREFIX': {'@namespace': u'http://openconfig.net/yang/network-instance-types', '@module': u'openconfig-network-instance-types'}, u'PER_NEXTHOP': {'@namespace': u'http://openconfig.net/yang/network-instance-types', '@module': u'openconfig-network-instance-types'}},), is_leaf=True, yang_name="label-allocation-mode", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='identityref', is_config=True)


  def _get_control_word(self):
    """
    Getter method for control_word, mapped from YANG variable /network_instances/network_instance/encapsulation/config/control_word (boolean)

    YANG Description: Whether the control-word should be used for the network
instance
    """
    return self.__control_word
      
  def _set_control_word(self, v, load=False):
    """
    Setter method for control_word, mapped from YANG variable /network_instances/network_instance/encapsulation/config/control_word (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_control_word is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_control_word() directly.

    YANG Description: Whether the control-word should be used for the network
instance
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="control-word", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """control_word must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="control-word", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)""",
        })

    self.__control_word = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_control_word(self):
    self.__control_word = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="control-word", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)

  encapsulation_type = __builtin__.property(_get_encapsulation_type, _set_encapsulation_type)
  label_allocation_mode = __builtin__.property(_get_label_allocation_mode, _set_label_allocation_mode)
  control_word = __builtin__.property(_get_control_word, _set_control_word)


  _pyangbind_elements = {'encapsulation_type': encapsulation_type, 'label_allocation_mode': label_allocation_mode, 'control_word': control_word, }


