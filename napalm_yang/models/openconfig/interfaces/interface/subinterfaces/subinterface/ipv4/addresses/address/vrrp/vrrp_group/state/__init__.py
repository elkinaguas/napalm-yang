
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

class state(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-interfaces - based on the path /interfaces/interface/subinterfaces/subinterface/ipv4/addresses/address/vrrp/vrrp-group/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Operational state data for the VRRP group
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__virtual_router_id','__virtual_address','__priority','__preempt','__preempt_delay','__accept_mode','__advertisement_interval','__current_priority',)

  _yang_name = 'state'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__current_priority = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="current-priority", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/ip', defining_module='openconfig-if-ip', yang_type='uint8', is_config=False)
    self.__virtual_address = YANGDynClass(base=TypedListType(allowed_type=[RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}),RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'^(([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:))$'}),]), is_leaf=False, yang_name="virtual-address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/ip', defining_module='openconfig-if-ip', yang_type='oc-inet:ip-address', is_config=False)
    self.__priority = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': [u'1..254']}), default=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8)(100), is_leaf=True, yang_name="priority", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/ip', defining_module='openconfig-if-ip', yang_type='uint8', is_config=False)
    self.__preempt = YANGDynClass(base=YANGBool, default=YANGBool("true"), is_leaf=True, yang_name="preempt", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/ip', defining_module='openconfig-if-ip', yang_type='boolean', is_config=False)
    self.__advertisement_interval = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': [u'1..4095']}), default=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16)(100), is_leaf=True, yang_name="advertisement-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/ip', defining_module='openconfig-if-ip', yang_type='uint16', is_config=False)
    self.__virtual_router_id = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': [u'1..255']}), is_leaf=True, yang_name="virtual-router-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/ip', defining_module='openconfig-if-ip', yang_type='uint8', is_config=False)
    self.__preempt_delay = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': [u'0..3600']}), default=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16)(0), is_leaf=True, yang_name="preempt-delay", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/ip', defining_module='openconfig-if-ip', yang_type='uint16', is_config=False)
    self.__accept_mode = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="accept-mode", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/ip', defining_module='openconfig-if-ip', yang_type='boolean', is_config=False)

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
      return [u'interfaces', u'interface', u'subinterfaces', u'subinterface', u'ipv4', u'addresses', u'address', u'vrrp', u'vrrp-group', u'state']

  def _get_virtual_router_id(self):
    """
    Getter method for virtual_router_id, mapped from YANG variable /interfaces/interface/subinterfaces/subinterface/ipv4/addresses/address/vrrp/vrrp_group/state/virtual_router_id (uint8)

    YANG Description: Set the virtual router id for use by the VRRP group.  This
usually also determines the virtual MAC address that is
generated for the VRRP group
    """
    return self.__virtual_router_id
      
  def _set_virtual_router_id(self, v, load=False):
    """
    Setter method for virtual_router_id, mapped from YANG variable /interfaces/interface/subinterfaces/subinterface/ipv4/addresses/address/vrrp/vrrp_group/state/virtual_router_id (uint8)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_virtual_router_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_virtual_router_id() directly.

    YANG Description: Set the virtual router id for use by the VRRP group.  This
usually also determines the virtual MAC address that is
generated for the VRRP group
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': [u'1..255']}), is_leaf=True, yang_name="virtual-router-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/ip', defining_module='openconfig-if-ip', yang_type='uint8', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """virtual_router_id must be of a type compatible with uint8""",
          'defined-type': "uint8",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': [u'1..255']}), is_leaf=True, yang_name="virtual-router-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/ip', defining_module='openconfig-if-ip', yang_type='uint8', is_config=False)""",
        })

    self.__virtual_router_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_virtual_router_id(self):
    self.__virtual_router_id = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': [u'1..255']}), is_leaf=True, yang_name="virtual-router-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/ip', defining_module='openconfig-if-ip', yang_type='uint8', is_config=False)


  def _get_virtual_address(self):
    """
    Getter method for virtual_address, mapped from YANG variable /interfaces/interface/subinterfaces/subinterface/ipv4/addresses/address/vrrp/vrrp_group/state/virtual_address (oc-inet:ip-address)

    YANG Description: Configure one or more virtual addresses for the
VRRP group
    """
    return self.__virtual_address
      
  def _set_virtual_address(self, v, load=False):
    """
    Setter method for virtual_address, mapped from YANG variable /interfaces/interface/subinterfaces/subinterface/ipv4/addresses/address/vrrp/vrrp_group/state/virtual_address (oc-inet:ip-address)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_virtual_address is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_virtual_address() directly.

    YANG Description: Configure one or more virtual addresses for the
VRRP group
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=TypedListType(allowed_type=[RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}),RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'^(([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:))$'}),]), is_leaf=False, yang_name="virtual-address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/ip', defining_module='openconfig-if-ip', yang_type='oc-inet:ip-address', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """virtual_address must be of a type compatible with oc-inet:ip-address""",
          'defined-type': "oc-inet:ip-address",
          'generated-type': """YANGDynClass(base=TypedListType(allowed_type=[RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}),RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'^(([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:))$'}),]), is_leaf=False, yang_name="virtual-address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/ip', defining_module='openconfig-if-ip', yang_type='oc-inet:ip-address', is_config=False)""",
        })

    self.__virtual_address = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_virtual_address(self):
    self.__virtual_address = YANGDynClass(base=TypedListType(allowed_type=[RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}),RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'^(([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:))$'}),]), is_leaf=False, yang_name="virtual-address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/ip', defining_module='openconfig-if-ip', yang_type='oc-inet:ip-address', is_config=False)


  def _get_priority(self):
    """
    Getter method for priority, mapped from YANG variable /interfaces/interface/subinterfaces/subinterface/ipv4/addresses/address/vrrp/vrrp_group/state/priority (uint8)

    YANG Description: Specifies the sending VRRP interface's priority
for the virtual router.  Higher values equal higher
priority
    """
    return self.__priority
      
  def _set_priority(self, v, load=False):
    """
    Setter method for priority, mapped from YANG variable /interfaces/interface/subinterfaces/subinterface/ipv4/addresses/address/vrrp/vrrp_group/state/priority (uint8)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_priority is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_priority() directly.

    YANG Description: Specifies the sending VRRP interface's priority
for the virtual router.  Higher values equal higher
priority
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': [u'1..254']}), default=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8)(100), is_leaf=True, yang_name="priority", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/ip', defining_module='openconfig-if-ip', yang_type='uint8', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """priority must be of a type compatible with uint8""",
          'defined-type': "uint8",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': [u'1..254']}), default=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8)(100), is_leaf=True, yang_name="priority", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/ip', defining_module='openconfig-if-ip', yang_type='uint8', is_config=False)""",
        })

    self.__priority = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_priority(self):
    self.__priority = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': [u'1..254']}), default=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8)(100), is_leaf=True, yang_name="priority", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/ip', defining_module='openconfig-if-ip', yang_type='uint8', is_config=False)


  def _get_preempt(self):
    """
    Getter method for preempt, mapped from YANG variable /interfaces/interface/subinterfaces/subinterface/ipv4/addresses/address/vrrp/vrrp_group/state/preempt (boolean)

    YANG Description: When set to true, enables preemption by a higher
priority backup router of a lower priority master router
    """
    return self.__preempt
      
  def _set_preempt(self, v, load=False):
    """
    Setter method for preempt, mapped from YANG variable /interfaces/interface/subinterfaces/subinterface/ipv4/addresses/address/vrrp/vrrp_group/state/preempt (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_preempt is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_preempt() directly.

    YANG Description: When set to true, enables preemption by a higher
priority backup router of a lower priority master router
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, default=YANGBool("true"), is_leaf=True, yang_name="preempt", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/ip', defining_module='openconfig-if-ip', yang_type='boolean', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """preempt must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, default=YANGBool("true"), is_leaf=True, yang_name="preempt", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/ip', defining_module='openconfig-if-ip', yang_type='boolean', is_config=False)""",
        })

    self.__preempt = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_preempt(self):
    self.__preempt = YANGDynClass(base=YANGBool, default=YANGBool("true"), is_leaf=True, yang_name="preempt", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/ip', defining_module='openconfig-if-ip', yang_type='boolean', is_config=False)


  def _get_preempt_delay(self):
    """
    Getter method for preempt_delay, mapped from YANG variable /interfaces/interface/subinterfaces/subinterface/ipv4/addresses/address/vrrp/vrrp_group/state/preempt_delay (uint16)

    YANG Description: Set the delay the higher priority router waits
before preempting
    """
    return self.__preempt_delay
      
  def _set_preempt_delay(self, v, load=False):
    """
    Setter method for preempt_delay, mapped from YANG variable /interfaces/interface/subinterfaces/subinterface/ipv4/addresses/address/vrrp/vrrp_group/state/preempt_delay (uint16)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_preempt_delay is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_preempt_delay() directly.

    YANG Description: Set the delay the higher priority router waits
before preempting
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': [u'0..3600']}), default=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16)(0), is_leaf=True, yang_name="preempt-delay", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/ip', defining_module='openconfig-if-ip', yang_type='uint16', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """preempt_delay must be of a type compatible with uint16""",
          'defined-type': "uint16",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': [u'0..3600']}), default=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16)(0), is_leaf=True, yang_name="preempt-delay", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/ip', defining_module='openconfig-if-ip', yang_type='uint16', is_config=False)""",
        })

    self.__preempt_delay = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_preempt_delay(self):
    self.__preempt_delay = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': [u'0..3600']}), default=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16)(0), is_leaf=True, yang_name="preempt-delay", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/ip', defining_module='openconfig-if-ip', yang_type='uint16', is_config=False)


  def _get_accept_mode(self):
    """
    Getter method for accept_mode, mapped from YANG variable /interfaces/interface/subinterfaces/subinterface/ipv4/addresses/address/vrrp/vrrp_group/state/accept_mode (boolean)

    YANG Description: Configure whether packets destined for
virtual addresses are accepted even when the virtual
address is not owned by the router interface
    """
    return self.__accept_mode
      
  def _set_accept_mode(self, v, load=False):
    """
    Setter method for accept_mode, mapped from YANG variable /interfaces/interface/subinterfaces/subinterface/ipv4/addresses/address/vrrp/vrrp_group/state/accept_mode (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_accept_mode is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_accept_mode() directly.

    YANG Description: Configure whether packets destined for
virtual addresses are accepted even when the virtual
address is not owned by the router interface
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="accept-mode", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/ip', defining_module='openconfig-if-ip', yang_type='boolean', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """accept_mode must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="accept-mode", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/ip', defining_module='openconfig-if-ip', yang_type='boolean', is_config=False)""",
        })

    self.__accept_mode = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_accept_mode(self):
    self.__accept_mode = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="accept-mode", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/ip', defining_module='openconfig-if-ip', yang_type='boolean', is_config=False)


  def _get_advertisement_interval(self):
    """
    Getter method for advertisement_interval, mapped from YANG variable /interfaces/interface/subinterfaces/subinterface/ipv4/addresses/address/vrrp/vrrp_group/state/advertisement_interval (uint16)

    YANG Description: Sets the interval between successive VRRP
advertisements -- RFC 5798 defines this as a 12-bit
value expressed as 0.1 seconds, with default 100, i.e.,
1 second.  Several implementation express this in units of
seconds
    """
    return self.__advertisement_interval
      
  def _set_advertisement_interval(self, v, load=False):
    """
    Setter method for advertisement_interval, mapped from YANG variable /interfaces/interface/subinterfaces/subinterface/ipv4/addresses/address/vrrp/vrrp_group/state/advertisement_interval (uint16)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_advertisement_interval is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_advertisement_interval() directly.

    YANG Description: Sets the interval between successive VRRP
advertisements -- RFC 5798 defines this as a 12-bit
value expressed as 0.1 seconds, with default 100, i.e.,
1 second.  Several implementation express this in units of
seconds
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': [u'1..4095']}), default=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16)(100), is_leaf=True, yang_name="advertisement-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/ip', defining_module='openconfig-if-ip', yang_type='uint16', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """advertisement_interval must be of a type compatible with uint16""",
          'defined-type': "uint16",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': [u'1..4095']}), default=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16)(100), is_leaf=True, yang_name="advertisement-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/ip', defining_module='openconfig-if-ip', yang_type='uint16', is_config=False)""",
        })

    self.__advertisement_interval = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_advertisement_interval(self):
    self.__advertisement_interval = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': [u'1..4095']}), default=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16)(100), is_leaf=True, yang_name="advertisement-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/ip', defining_module='openconfig-if-ip', yang_type='uint16', is_config=False)


  def _get_current_priority(self):
    """
    Getter method for current_priority, mapped from YANG variable /interfaces/interface/subinterfaces/subinterface/ipv4/addresses/address/vrrp/vrrp_group/state/current_priority (uint8)

    YANG Description: Operational value of the priority for the
interface in the VRRP group
    """
    return self.__current_priority
      
  def _set_current_priority(self, v, load=False):
    """
    Setter method for current_priority, mapped from YANG variable /interfaces/interface/subinterfaces/subinterface/ipv4/addresses/address/vrrp/vrrp_group/state/current_priority (uint8)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_current_priority is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_current_priority() directly.

    YANG Description: Operational value of the priority for the
interface in the VRRP group
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="current-priority", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/ip', defining_module='openconfig-if-ip', yang_type='uint8', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """current_priority must be of a type compatible with uint8""",
          'defined-type': "uint8",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="current-priority", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/ip', defining_module='openconfig-if-ip', yang_type='uint8', is_config=False)""",
        })

    self.__current_priority = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_current_priority(self):
    self.__current_priority = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="current-priority", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/ip', defining_module='openconfig-if-ip', yang_type='uint8', is_config=False)

  virtual_router_id = __builtin__.property(_get_virtual_router_id)
  virtual_address = __builtin__.property(_get_virtual_address)
  priority = __builtin__.property(_get_priority)
  preempt = __builtin__.property(_get_preempt)
  preempt_delay = __builtin__.property(_get_preempt_delay)
  accept_mode = __builtin__.property(_get_accept_mode)
  advertisement_interval = __builtin__.property(_get_advertisement_interval)
  current_priority = __builtin__.property(_get_current_priority)


  _pyangbind_elements = {'virtual_router_id': virtual_router_id, 'virtual_address': virtual_address, 'priority': priority, 'preempt': preempt, 'preempt_delay': preempt_delay, 'accept_mode': accept_mode, 'advertisement_interval': advertisement_interval, 'current_priority': current_priority, }


