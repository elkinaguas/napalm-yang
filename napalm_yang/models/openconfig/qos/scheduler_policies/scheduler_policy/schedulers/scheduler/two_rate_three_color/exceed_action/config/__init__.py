
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
  from YANG module openconfig-qos - based on the path /qos/scheduler-policies/scheduler-policy/schedulers/scheduler/two-rate-three-color/exceed-action/config. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Configuration parameters relating to the action
applied to exceeding packets.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__set_dscp','__set_dot1p','__set_mpls_tc','__drop',)

  _yang_name = 'config'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__set_dscp = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="set-dscp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/qos', defining_module='openconfig-qos', yang_type='uint8', is_config=True)
    self.__set_dot1p = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="set-dot1p", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/qos', defining_module='openconfig-qos', yang_type='uint8', is_config=True)
    self.__drop = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="drop", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/qos', defining_module='openconfig-qos', yang_type='boolean', is_config=True)
    self.__set_mpls_tc = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="set-mpls-tc", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/qos', defining_module='openconfig-qos', yang_type='uint8', is_config=True)

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
      return [u'qos', u'scheduler-policies', u'scheduler-policy', u'schedulers', u'scheduler', u'two-rate-three-color', u'exceed-action', u'config']

  def _get_set_dscp(self):
    """
    Getter method for set_dscp, mapped from YANG variable /qos/scheduler_policies/scheduler_policy/schedulers/scheduler/two_rate_three_color/exceed_action/config/set_dscp (uint8)

    YANG Description: Sets the 6-bit DSCP (differentiated services code point)
value in the IP packet header.
    """
    return self.__set_dscp
      
  def _set_set_dscp(self, v, load=False):
    """
    Setter method for set_dscp, mapped from YANG variable /qos/scheduler_policies/scheduler_policy/schedulers/scheduler/two_rate_three_color/exceed_action/config/set_dscp (uint8)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_set_dscp is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_set_dscp() directly.

    YANG Description: Sets the 6-bit DSCP (differentiated services code point)
value in the IP packet header.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="set-dscp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/qos', defining_module='openconfig-qos', yang_type='uint8', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """set_dscp must be of a type compatible with uint8""",
          'defined-type': "uint8",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="set-dscp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/qos', defining_module='openconfig-qos', yang_type='uint8', is_config=True)""",
        })

    self.__set_dscp = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_set_dscp(self):
    self.__set_dscp = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="set-dscp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/qos', defining_module='openconfig-qos', yang_type='uint8', is_config=True)


  def _get_set_dot1p(self):
    """
    Getter method for set_dot1p, mapped from YANG variable /qos/scheduler_policies/scheduler_policy/schedulers/scheduler/two_rate_three_color/exceed_action/config/set_dot1p (uint8)

    YANG Description: Sets the 3-bit class-of-service value in the
Ethernet packet header for 802.1Q VLAN-tagged packets,
also known as PCP (priority code point).
    """
    return self.__set_dot1p
      
  def _set_set_dot1p(self, v, load=False):
    """
    Setter method for set_dot1p, mapped from YANG variable /qos/scheduler_policies/scheduler_policy/schedulers/scheduler/two_rate_three_color/exceed_action/config/set_dot1p (uint8)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_set_dot1p is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_set_dot1p() directly.

    YANG Description: Sets the 3-bit class-of-service value in the
Ethernet packet header for 802.1Q VLAN-tagged packets,
also known as PCP (priority code point).
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="set-dot1p", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/qos', defining_module='openconfig-qos', yang_type='uint8', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """set_dot1p must be of a type compatible with uint8""",
          'defined-type': "uint8",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="set-dot1p", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/qos', defining_module='openconfig-qos', yang_type='uint8', is_config=True)""",
        })

    self.__set_dot1p = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_set_dot1p(self):
    self.__set_dot1p = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="set-dot1p", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/qos', defining_module='openconfig-qos', yang_type='uint8', is_config=True)


  def _get_set_mpls_tc(self):
    """
    Getter method for set_mpls_tc, mapped from YANG variable /qos/scheduler_policies/scheduler_policy/schedulers/scheduler/two_rate_three_color/exceed_action/config/set_mpls_tc (uint8)

    YANG Description: Sets the 3-bit traffic class value (also referred to as EXP
or CoS) in MPLS packets.
    """
    return self.__set_mpls_tc
      
  def _set_set_mpls_tc(self, v, load=False):
    """
    Setter method for set_mpls_tc, mapped from YANG variable /qos/scheduler_policies/scheduler_policy/schedulers/scheduler/two_rate_three_color/exceed_action/config/set_mpls_tc (uint8)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_set_mpls_tc is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_set_mpls_tc() directly.

    YANG Description: Sets the 3-bit traffic class value (also referred to as EXP
or CoS) in MPLS packets.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="set-mpls-tc", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/qos', defining_module='openconfig-qos', yang_type='uint8', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """set_mpls_tc must be of a type compatible with uint8""",
          'defined-type': "uint8",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="set-mpls-tc", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/qos', defining_module='openconfig-qos', yang_type='uint8', is_config=True)""",
        })

    self.__set_mpls_tc = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_set_mpls_tc(self):
    self.__set_mpls_tc = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="set-mpls-tc", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/qos', defining_module='openconfig-qos', yang_type='uint8', is_config=True)


  def _get_drop(self):
    """
    Getter method for drop, mapped from YANG variable /qos/scheduler_policies/scheduler_policy/schedulers/scheduler/two_rate_three_color/exceed_action/config/drop (boolean)

    YANG Description: If set to true, packets within this context are dropped.
    """
    return self.__drop
      
  def _set_drop(self, v, load=False):
    """
    Setter method for drop, mapped from YANG variable /qos/scheduler_policies/scheduler_policy/schedulers/scheduler/two_rate_three_color/exceed_action/config/drop (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_drop is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_drop() directly.

    YANG Description: If set to true, packets within this context are dropped.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="drop", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/qos', defining_module='openconfig-qos', yang_type='boolean', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """drop must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="drop", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/qos', defining_module='openconfig-qos', yang_type='boolean', is_config=True)""",
        })

    self.__drop = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_drop(self):
    self.__drop = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="drop", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/qos', defining_module='openconfig-qos', yang_type='boolean', is_config=True)

  set_dscp = __builtin__.property(_get_set_dscp, _set_set_dscp)
  set_dot1p = __builtin__.property(_get_set_dot1p, _set_set_dot1p)
  set_mpls_tc = __builtin__.property(_get_set_mpls_tc, _set_set_mpls_tc)
  drop = __builtin__.property(_get_drop, _set_drop)


  _pyangbind_elements = {'set_dscp': set_dscp, 'set_dot1p': set_dot1p, 'set_mpls_tc': set_mpls_tc, 'drop': drop, }


class config(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-qos-interfaces - based on the path /qos/scheduler-policies/scheduler-policy/schedulers/scheduler/two-rate-three-color/exceed-action/config. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Configuration parameters relating to the action
applied to exceeding packets.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__set_dscp','__set_dot1p','__set_mpls_tc','__drop',)

  _yang_name = 'config'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__set_dscp = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="set-dscp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/qos', defining_module='openconfig-qos', yang_type='uint8', is_config=True)
    self.__set_dot1p = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="set-dot1p", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/qos', defining_module='openconfig-qos', yang_type='uint8', is_config=True)
    self.__drop = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="drop", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/qos', defining_module='openconfig-qos', yang_type='boolean', is_config=True)
    self.__set_mpls_tc = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="set-mpls-tc", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/qos', defining_module='openconfig-qos', yang_type='uint8', is_config=True)

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
      return [u'qos', u'scheduler-policies', u'scheduler-policy', u'schedulers', u'scheduler', u'two-rate-three-color', u'exceed-action', u'config']

  def _get_set_dscp(self):
    """
    Getter method for set_dscp, mapped from YANG variable /qos/scheduler_policies/scheduler_policy/schedulers/scheduler/two_rate_three_color/exceed_action/config/set_dscp (uint8)

    YANG Description: Sets the 6-bit DSCP (differentiated services code point)
value in the IP packet header.
    """
    return self.__set_dscp
      
  def _set_set_dscp(self, v, load=False):
    """
    Setter method for set_dscp, mapped from YANG variable /qos/scheduler_policies/scheduler_policy/schedulers/scheduler/two_rate_three_color/exceed_action/config/set_dscp (uint8)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_set_dscp is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_set_dscp() directly.

    YANG Description: Sets the 6-bit DSCP (differentiated services code point)
value in the IP packet header.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="set-dscp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/qos', defining_module='openconfig-qos', yang_type='uint8', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """set_dscp must be of a type compatible with uint8""",
          'defined-type': "uint8",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="set-dscp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/qos', defining_module='openconfig-qos', yang_type='uint8', is_config=True)""",
        })

    self.__set_dscp = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_set_dscp(self):
    self.__set_dscp = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="set-dscp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/qos', defining_module='openconfig-qos', yang_type='uint8', is_config=True)


  def _get_set_dot1p(self):
    """
    Getter method for set_dot1p, mapped from YANG variable /qos/scheduler_policies/scheduler_policy/schedulers/scheduler/two_rate_three_color/exceed_action/config/set_dot1p (uint8)

    YANG Description: Sets the 3-bit class-of-service value in the
Ethernet packet header for 802.1Q VLAN-tagged packets,
also known as PCP (priority code point).
    """
    return self.__set_dot1p
      
  def _set_set_dot1p(self, v, load=False):
    """
    Setter method for set_dot1p, mapped from YANG variable /qos/scheduler_policies/scheduler_policy/schedulers/scheduler/two_rate_three_color/exceed_action/config/set_dot1p (uint8)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_set_dot1p is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_set_dot1p() directly.

    YANG Description: Sets the 3-bit class-of-service value in the
Ethernet packet header for 802.1Q VLAN-tagged packets,
also known as PCP (priority code point).
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="set-dot1p", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/qos', defining_module='openconfig-qos', yang_type='uint8', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """set_dot1p must be of a type compatible with uint8""",
          'defined-type': "uint8",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="set-dot1p", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/qos', defining_module='openconfig-qos', yang_type='uint8', is_config=True)""",
        })

    self.__set_dot1p = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_set_dot1p(self):
    self.__set_dot1p = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="set-dot1p", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/qos', defining_module='openconfig-qos', yang_type='uint8', is_config=True)


  def _get_set_mpls_tc(self):
    """
    Getter method for set_mpls_tc, mapped from YANG variable /qos/scheduler_policies/scheduler_policy/schedulers/scheduler/two_rate_three_color/exceed_action/config/set_mpls_tc (uint8)

    YANG Description: Sets the 3-bit traffic class value (also referred to as EXP
or CoS) in MPLS packets.
    """
    return self.__set_mpls_tc
      
  def _set_set_mpls_tc(self, v, load=False):
    """
    Setter method for set_mpls_tc, mapped from YANG variable /qos/scheduler_policies/scheduler_policy/schedulers/scheduler/two_rate_three_color/exceed_action/config/set_mpls_tc (uint8)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_set_mpls_tc is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_set_mpls_tc() directly.

    YANG Description: Sets the 3-bit traffic class value (also referred to as EXP
or CoS) in MPLS packets.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="set-mpls-tc", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/qos', defining_module='openconfig-qos', yang_type='uint8', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """set_mpls_tc must be of a type compatible with uint8""",
          'defined-type': "uint8",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="set-mpls-tc", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/qos', defining_module='openconfig-qos', yang_type='uint8', is_config=True)""",
        })

    self.__set_mpls_tc = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_set_mpls_tc(self):
    self.__set_mpls_tc = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="set-mpls-tc", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/qos', defining_module='openconfig-qos', yang_type='uint8', is_config=True)


  def _get_drop(self):
    """
    Getter method for drop, mapped from YANG variable /qos/scheduler_policies/scheduler_policy/schedulers/scheduler/two_rate_three_color/exceed_action/config/drop (boolean)

    YANG Description: If set to true, packets within this context are dropped.
    """
    return self.__drop
      
  def _set_drop(self, v, load=False):
    """
    Setter method for drop, mapped from YANG variable /qos/scheduler_policies/scheduler_policy/schedulers/scheduler/two_rate_three_color/exceed_action/config/drop (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_drop is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_drop() directly.

    YANG Description: If set to true, packets within this context are dropped.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="drop", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/qos', defining_module='openconfig-qos', yang_type='boolean', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """drop must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="drop", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/qos', defining_module='openconfig-qos', yang_type='boolean', is_config=True)""",
        })

    self.__drop = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_drop(self):
    self.__drop = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="drop", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/qos', defining_module='openconfig-qos', yang_type='boolean', is_config=True)

  set_dscp = __builtin__.property(_get_set_dscp, _set_set_dscp)
  set_dot1p = __builtin__.property(_get_set_dot1p, _set_set_dot1p)
  set_mpls_tc = __builtin__.property(_get_set_mpls_tc, _set_set_mpls_tc)
  drop = __builtin__.property(_get_drop, _set_drop)


  _pyangbind_elements = {'set_dscp': set_dscp, 'set_dot1p': set_dot1p, 'set_mpls_tc': set_mpls_tc, 'drop': drop, }


class config(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-qos-elements - based on the path /qos/scheduler-policies/scheduler-policy/schedulers/scheduler/two-rate-three-color/exceed-action/config. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Configuration parameters relating to the action
applied to exceeding packets.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__set_dscp','__set_dot1p','__set_mpls_tc','__drop',)

  _yang_name = 'config'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__set_dscp = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="set-dscp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/qos', defining_module='openconfig-qos', yang_type='uint8', is_config=True)
    self.__set_dot1p = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="set-dot1p", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/qos', defining_module='openconfig-qos', yang_type='uint8', is_config=True)
    self.__drop = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="drop", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/qos', defining_module='openconfig-qos', yang_type='boolean', is_config=True)
    self.__set_mpls_tc = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="set-mpls-tc", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/qos', defining_module='openconfig-qos', yang_type='uint8', is_config=True)

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
      return [u'qos', u'scheduler-policies', u'scheduler-policy', u'schedulers', u'scheduler', u'two-rate-three-color', u'exceed-action', u'config']

  def _get_set_dscp(self):
    """
    Getter method for set_dscp, mapped from YANG variable /qos/scheduler_policies/scheduler_policy/schedulers/scheduler/two_rate_three_color/exceed_action/config/set_dscp (uint8)

    YANG Description: Sets the 6-bit DSCP (differentiated services code point)
value in the IP packet header.
    """
    return self.__set_dscp
      
  def _set_set_dscp(self, v, load=False):
    """
    Setter method for set_dscp, mapped from YANG variable /qos/scheduler_policies/scheduler_policy/schedulers/scheduler/two_rate_three_color/exceed_action/config/set_dscp (uint8)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_set_dscp is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_set_dscp() directly.

    YANG Description: Sets the 6-bit DSCP (differentiated services code point)
value in the IP packet header.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="set-dscp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/qos', defining_module='openconfig-qos', yang_type='uint8', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """set_dscp must be of a type compatible with uint8""",
          'defined-type': "uint8",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="set-dscp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/qos', defining_module='openconfig-qos', yang_type='uint8', is_config=True)""",
        })

    self.__set_dscp = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_set_dscp(self):
    self.__set_dscp = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="set-dscp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/qos', defining_module='openconfig-qos', yang_type='uint8', is_config=True)


  def _get_set_dot1p(self):
    """
    Getter method for set_dot1p, mapped from YANG variable /qos/scheduler_policies/scheduler_policy/schedulers/scheduler/two_rate_three_color/exceed_action/config/set_dot1p (uint8)

    YANG Description: Sets the 3-bit class-of-service value in the
Ethernet packet header for 802.1Q VLAN-tagged packets,
also known as PCP (priority code point).
    """
    return self.__set_dot1p
      
  def _set_set_dot1p(self, v, load=False):
    """
    Setter method for set_dot1p, mapped from YANG variable /qos/scheduler_policies/scheduler_policy/schedulers/scheduler/two_rate_three_color/exceed_action/config/set_dot1p (uint8)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_set_dot1p is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_set_dot1p() directly.

    YANG Description: Sets the 3-bit class-of-service value in the
Ethernet packet header for 802.1Q VLAN-tagged packets,
also known as PCP (priority code point).
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="set-dot1p", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/qos', defining_module='openconfig-qos', yang_type='uint8', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """set_dot1p must be of a type compatible with uint8""",
          'defined-type': "uint8",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="set-dot1p", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/qos', defining_module='openconfig-qos', yang_type='uint8', is_config=True)""",
        })

    self.__set_dot1p = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_set_dot1p(self):
    self.__set_dot1p = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="set-dot1p", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/qos', defining_module='openconfig-qos', yang_type='uint8', is_config=True)


  def _get_set_mpls_tc(self):
    """
    Getter method for set_mpls_tc, mapped from YANG variable /qos/scheduler_policies/scheduler_policy/schedulers/scheduler/two_rate_three_color/exceed_action/config/set_mpls_tc (uint8)

    YANG Description: Sets the 3-bit traffic class value (also referred to as EXP
or CoS) in MPLS packets.
    """
    return self.__set_mpls_tc
      
  def _set_set_mpls_tc(self, v, load=False):
    """
    Setter method for set_mpls_tc, mapped from YANG variable /qos/scheduler_policies/scheduler_policy/schedulers/scheduler/two_rate_three_color/exceed_action/config/set_mpls_tc (uint8)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_set_mpls_tc is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_set_mpls_tc() directly.

    YANG Description: Sets the 3-bit traffic class value (also referred to as EXP
or CoS) in MPLS packets.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="set-mpls-tc", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/qos', defining_module='openconfig-qos', yang_type='uint8', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """set_mpls_tc must be of a type compatible with uint8""",
          'defined-type': "uint8",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="set-mpls-tc", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/qos', defining_module='openconfig-qos', yang_type='uint8', is_config=True)""",
        })

    self.__set_mpls_tc = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_set_mpls_tc(self):
    self.__set_mpls_tc = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="set-mpls-tc", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/qos', defining_module='openconfig-qos', yang_type='uint8', is_config=True)


  def _get_drop(self):
    """
    Getter method for drop, mapped from YANG variable /qos/scheduler_policies/scheduler_policy/schedulers/scheduler/two_rate_three_color/exceed_action/config/drop (boolean)

    YANG Description: If set to true, packets within this context are dropped.
    """
    return self.__drop
      
  def _set_drop(self, v, load=False):
    """
    Setter method for drop, mapped from YANG variable /qos/scheduler_policies/scheduler_policy/schedulers/scheduler/two_rate_three_color/exceed_action/config/drop (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_drop is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_drop() directly.

    YANG Description: If set to true, packets within this context are dropped.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="drop", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/qos', defining_module='openconfig-qos', yang_type='boolean', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """drop must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="drop", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/qos', defining_module='openconfig-qos', yang_type='boolean', is_config=True)""",
        })

    self.__drop = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_drop(self):
    self.__drop = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="drop", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/qos', defining_module='openconfig-qos', yang_type='boolean', is_config=True)

  set_dscp = __builtin__.property(_get_set_dscp, _set_set_dscp)
  set_dot1p = __builtin__.property(_get_set_dot1p, _set_set_dot1p)
  set_mpls_tc = __builtin__.property(_get_set_mpls_tc, _set_set_mpls_tc)
  drop = __builtin__.property(_get_drop, _set_drop)


  _pyangbind_elements = {'set_dscp': set_dscp, 'set_dot1p': set_dot1p, 'set_mpls_tc': set_mpls_tc, 'drop': drop, }


