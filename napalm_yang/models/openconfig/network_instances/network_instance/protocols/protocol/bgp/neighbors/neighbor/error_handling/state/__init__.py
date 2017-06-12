
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
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/protocols/protocol/bgp/neighbors/neighbor/error-handling/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: State information relating to enhanced error handling
mechanisms for the BGP neighbor
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__treat_as_withdraw','__erroneous_update_messages',)

  _yang_name = 'state'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__erroneous_update_messages = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="erroneous-update-messages", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint32', is_config=False)
    self.__treat_as_withdraw = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="treat-as-withdraw", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=False)

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
      return [u'network-instances', u'network-instance', u'protocols', u'protocol', u'bgp', u'neighbors', u'neighbor', u'error-handling', u'state']

  def _get_treat_as_withdraw(self):
    """
    Getter method for treat_as_withdraw, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/neighbors/neighbor/error_handling/state/treat_as_withdraw (boolean)

    YANG Description: Specify whether erroneous UPDATE messages for which the
NLRI can be extracted are reated as though the NLRI is
withdrawn - avoiding session reset
    """
    return self.__treat_as_withdraw
      
  def _set_treat_as_withdraw(self, v, load=False):
    """
    Setter method for treat_as_withdraw, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/neighbors/neighbor/error_handling/state/treat_as_withdraw (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_treat_as_withdraw is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_treat_as_withdraw() directly.

    YANG Description: Specify whether erroneous UPDATE messages for which the
NLRI can be extracted are reated as though the NLRI is
withdrawn - avoiding session reset
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="treat-as-withdraw", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """treat_as_withdraw must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="treat-as-withdraw", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=False)""",
        })

    self.__treat_as_withdraw = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_treat_as_withdraw(self):
    self.__treat_as_withdraw = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="treat-as-withdraw", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=False)


  def _get_erroneous_update_messages(self):
    """
    Getter method for erroneous_update_messages, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/neighbors/neighbor/error_handling/state/erroneous_update_messages (uint32)

    YANG Description: The number of BGP UPDATE messages for which the
treat-as-withdraw mechanism has been applied based
on erroneous message contents
    """
    return self.__erroneous_update_messages
      
  def _set_erroneous_update_messages(self, v, load=False):
    """
    Setter method for erroneous_update_messages, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/neighbors/neighbor/error_handling/state/erroneous_update_messages (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_erroneous_update_messages is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_erroneous_update_messages() directly.

    YANG Description: The number of BGP UPDATE messages for which the
treat-as-withdraw mechanism has been applied based
on erroneous message contents
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="erroneous-update-messages", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """erroneous_update_messages must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="erroneous-update-messages", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint32', is_config=False)""",
        })

    self.__erroneous_update_messages = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_erroneous_update_messages(self):
    self.__erroneous_update_messages = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="erroneous-update-messages", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint32', is_config=False)

  treat_as_withdraw = __builtin__.property(_get_treat_as_withdraw)
  erroneous_update_messages = __builtin__.property(_get_erroneous_update_messages)


  _pyangbind_elements = {'treat_as_withdraw': treat_as_withdraw, 'erroneous_update_messages': erroneous_update_messages, }


class state(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/protocols/protocol/bgp/neighbors/neighbor/error-handling/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: State information relating to enhanced error handling
mechanisms for the BGP neighbor
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__treat_as_withdraw','__erroneous_update_messages',)

  _yang_name = 'state'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__erroneous_update_messages = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="erroneous-update-messages", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint32', is_config=False)
    self.__treat_as_withdraw = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="treat-as-withdraw", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=False)

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
      return [u'network-instances', u'network-instance', u'protocols', u'protocol', u'bgp', u'neighbors', u'neighbor', u'error-handling', u'state']

  def _get_treat_as_withdraw(self):
    """
    Getter method for treat_as_withdraw, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/neighbors/neighbor/error_handling/state/treat_as_withdraw (boolean)

    YANG Description: Specify whether erroneous UPDATE messages for which the
NLRI can be extracted are reated as though the NLRI is
withdrawn - avoiding session reset
    """
    return self.__treat_as_withdraw
      
  def _set_treat_as_withdraw(self, v, load=False):
    """
    Setter method for treat_as_withdraw, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/neighbors/neighbor/error_handling/state/treat_as_withdraw (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_treat_as_withdraw is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_treat_as_withdraw() directly.

    YANG Description: Specify whether erroneous UPDATE messages for which the
NLRI can be extracted are reated as though the NLRI is
withdrawn - avoiding session reset
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="treat-as-withdraw", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """treat_as_withdraw must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="treat-as-withdraw", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=False)""",
        })

    self.__treat_as_withdraw = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_treat_as_withdraw(self):
    self.__treat_as_withdraw = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="treat-as-withdraw", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=False)


  def _get_erroneous_update_messages(self):
    """
    Getter method for erroneous_update_messages, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/neighbors/neighbor/error_handling/state/erroneous_update_messages (uint32)

    YANG Description: The number of BGP UPDATE messages for which the
treat-as-withdraw mechanism has been applied based
on erroneous message contents
    """
    return self.__erroneous_update_messages
      
  def _set_erroneous_update_messages(self, v, load=False):
    """
    Setter method for erroneous_update_messages, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/neighbors/neighbor/error_handling/state/erroneous_update_messages (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_erroneous_update_messages is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_erroneous_update_messages() directly.

    YANG Description: The number of BGP UPDATE messages for which the
treat-as-withdraw mechanism has been applied based
on erroneous message contents
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="erroneous-update-messages", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """erroneous_update_messages must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="erroneous-update-messages", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint32', is_config=False)""",
        })

    self.__erroneous_update_messages = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_erroneous_update_messages(self):
    self.__erroneous_update_messages = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="erroneous-update-messages", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint32', is_config=False)

  treat_as_withdraw = __builtin__.property(_get_treat_as_withdraw)
  erroneous_update_messages = __builtin__.property(_get_erroneous_update_messages)


  _pyangbind_elements = {'treat_as_withdraw': treat_as_withdraw, 'erroneous_update_messages': erroneous_update_messages, }


