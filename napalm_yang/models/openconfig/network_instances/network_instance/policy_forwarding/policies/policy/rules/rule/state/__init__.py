
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

class state(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/policy-forwarding/policies/policy/rules/rule/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Operational state parameters relating to the match
rule.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__sequence_id','__matched_pkts','__matched_octets',)

  _yang_name = 'state'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__sequence_id = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="sequence-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint32', is_config=False)
    self.__matched_octets = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="matched-octets", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='yang:counter64', is_config=False)
    self.__matched_pkts = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="matched-pkts", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='yang:counter64', is_config=False)

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
      return [u'network-instances', u'network-instance', u'policy-forwarding', u'policies', u'policy', u'rules', u'rule', u'state']

  def _get_sequence_id(self):
    """
    Getter method for sequence_id, mapped from YANG variable /network_instances/network_instance/policy_forwarding/policies/policy/rules/rule/state/sequence_id (uint32)

    YANG Description: Unique sequence number for the policy rule.
    """
    return self.__sequence_id
      
  def _set_sequence_id(self, v, load=False):
    """
    Setter method for sequence_id, mapped from YANG variable /network_instances/network_instance/policy_forwarding/policies/policy/rules/rule/state/sequence_id (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_sequence_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_sequence_id() directly.

    YANG Description: Unique sequence number for the policy rule.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="sequence-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """sequence_id must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="sequence-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint32', is_config=False)""",
        })

    self.__sequence_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_sequence_id(self):
    self.__sequence_id = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="sequence-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint32', is_config=False)


  def _get_matched_pkts(self):
    """
    Getter method for matched_pkts, mapped from YANG variable /network_instances/network_instance/policy_forwarding/policies/policy/rules/rule/state/matched_pkts (yang:counter64)

    YANG Description: Number of packets matched by the rule.
    """
    return self.__matched_pkts
      
  def _set_matched_pkts(self, v, load=False):
    """
    Setter method for matched_pkts, mapped from YANG variable /network_instances/network_instance/policy_forwarding/policies/policy/rules/rule/state/matched_pkts (yang:counter64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_matched_pkts is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_matched_pkts() directly.

    YANG Description: Number of packets matched by the rule.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="matched-pkts", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='yang:counter64', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """matched_pkts must be of a type compatible with yang:counter64""",
          'defined-type': "yang:counter64",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="matched-pkts", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='yang:counter64', is_config=False)""",
        })

    self.__matched_pkts = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_matched_pkts(self):
    self.__matched_pkts = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="matched-pkts", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='yang:counter64', is_config=False)


  def _get_matched_octets(self):
    """
    Getter method for matched_octets, mapped from YANG variable /network_instances/network_instance/policy_forwarding/policies/policy/rules/rule/state/matched_octets (yang:counter64)

    YANG Description: Bytes matched by the rule.
    """
    return self.__matched_octets
      
  def _set_matched_octets(self, v, load=False):
    """
    Setter method for matched_octets, mapped from YANG variable /network_instances/network_instance/policy_forwarding/policies/policy/rules/rule/state/matched_octets (yang:counter64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_matched_octets is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_matched_octets() directly.

    YANG Description: Bytes matched by the rule.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="matched-octets", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='yang:counter64', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """matched_octets must be of a type compatible with yang:counter64""",
          'defined-type': "yang:counter64",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="matched-octets", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='yang:counter64', is_config=False)""",
        })

    self.__matched_octets = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_matched_octets(self):
    self.__matched_octets = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="matched-octets", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='yang:counter64', is_config=False)

  sequence_id = __builtin__.property(_get_sequence_id)
  matched_pkts = __builtin__.property(_get_matched_pkts)
  matched_octets = __builtin__.property(_get_matched_octets)


  _pyangbind_elements = {'sequence_id': sequence_id, 'matched_pkts': matched_pkts, 'matched_octets': matched_octets, }


class state(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/policy-forwarding/policies/policy/rules/rule/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Operational state parameters relating to the match
rule.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__sequence_id','__matched_pkts','__matched_octets',)

  _yang_name = 'state'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__sequence_id = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="sequence-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint32', is_config=False)
    self.__matched_octets = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="matched-octets", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='yang:counter64', is_config=False)
    self.__matched_pkts = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="matched-pkts", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='yang:counter64', is_config=False)

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
      return [u'network-instances', u'network-instance', u'policy-forwarding', u'policies', u'policy', u'rules', u'rule', u'state']

  def _get_sequence_id(self):
    """
    Getter method for sequence_id, mapped from YANG variable /network_instances/network_instance/policy_forwarding/policies/policy/rules/rule/state/sequence_id (uint32)

    YANG Description: Unique sequence number for the policy rule.
    """
    return self.__sequence_id
      
  def _set_sequence_id(self, v, load=False):
    """
    Setter method for sequence_id, mapped from YANG variable /network_instances/network_instance/policy_forwarding/policies/policy/rules/rule/state/sequence_id (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_sequence_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_sequence_id() directly.

    YANG Description: Unique sequence number for the policy rule.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="sequence-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """sequence_id must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="sequence-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint32', is_config=False)""",
        })

    self.__sequence_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_sequence_id(self):
    self.__sequence_id = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="sequence-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint32', is_config=False)


  def _get_matched_pkts(self):
    """
    Getter method for matched_pkts, mapped from YANG variable /network_instances/network_instance/policy_forwarding/policies/policy/rules/rule/state/matched_pkts (yang:counter64)

    YANG Description: Number of packets matched by the rule.
    """
    return self.__matched_pkts
      
  def _set_matched_pkts(self, v, load=False):
    """
    Setter method for matched_pkts, mapped from YANG variable /network_instances/network_instance/policy_forwarding/policies/policy/rules/rule/state/matched_pkts (yang:counter64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_matched_pkts is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_matched_pkts() directly.

    YANG Description: Number of packets matched by the rule.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="matched-pkts", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='yang:counter64', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """matched_pkts must be of a type compatible with yang:counter64""",
          'defined-type': "yang:counter64",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="matched-pkts", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='yang:counter64', is_config=False)""",
        })

    self.__matched_pkts = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_matched_pkts(self):
    self.__matched_pkts = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="matched-pkts", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='yang:counter64', is_config=False)


  def _get_matched_octets(self):
    """
    Getter method for matched_octets, mapped from YANG variable /network_instances/network_instance/policy_forwarding/policies/policy/rules/rule/state/matched_octets (yang:counter64)

    YANG Description: Bytes matched by the rule.
    """
    return self.__matched_octets
      
  def _set_matched_octets(self, v, load=False):
    """
    Setter method for matched_octets, mapped from YANG variable /network_instances/network_instance/policy_forwarding/policies/policy/rules/rule/state/matched_octets (yang:counter64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_matched_octets is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_matched_octets() directly.

    YANG Description: Bytes matched by the rule.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="matched-octets", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='yang:counter64', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """matched_octets must be of a type compatible with yang:counter64""",
          'defined-type': "yang:counter64",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="matched-octets", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='yang:counter64', is_config=False)""",
        })

    self.__matched_octets = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_matched_octets(self):
    self.__matched_octets = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="matched-octets", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='yang:counter64', is_config=False)

  sequence_id = __builtin__.property(_get_sequence_id)
  matched_pkts = __builtin__.property(_get_matched_pkts)
  matched_octets = __builtin__.property(_get_matched_octets)


  _pyangbind_elements = {'sequence_id': sequence_id, 'matched_pkts': matched_pkts, 'matched_octets': matched_octets, }


