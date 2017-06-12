
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

import aft
class afts(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/afts. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: The abstract forwarding tables (AFTs) that are associated
with the network instance. An AFT is instantiated per-protocol
running within the network-instance - such that one exists for
IPv4 Unicast, IPv6 Unicast, MPLS, L2 forwarding entries, etc.
A forwarding entry within the FIB has a set of next-hops,
which may be a reference to an entry within another table -
e.g., where a Layer 3 next-hop has an associated Layer 2
forwarding entry.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__aft',)

  _yang_name = 'afts'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__aft = YANGDynClass(base=YANGListType("address_family",aft.aft, yang_name="aft", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='address-family', extensions=None), is_container='list', yang_name="aft", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)

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
      return [u'network-instances', u'network-instance', u'afts']

  def _get_aft(self):
    """
    Getter method for aft, mapped from YANG variable /network_instances/network_instance/afts/aft (list)

    YANG Description: An individual abstract forwarding table associated with a
an address family wtihin the network instance.
    """
    return self.__aft
      
  def _set_aft(self, v, load=False):
    """
    Setter method for aft, mapped from YANG variable /network_instances/network_instance/afts/aft (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_aft is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_aft() directly.

    YANG Description: An individual abstract forwarding table associated with a
an address family wtihin the network instance.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("address_family",aft.aft, yang_name="aft", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='address-family', extensions=None), is_container='list', yang_name="aft", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """aft must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("address_family",aft.aft, yang_name="aft", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='address-family', extensions=None), is_container='list', yang_name="aft", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)""",
        })

    self.__aft = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_aft(self):
    self.__aft = YANGDynClass(base=YANGListType("address_family",aft.aft, yang_name="aft", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='address-family', extensions=None), is_container='list', yang_name="aft", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)

  aft = __builtin__.property(_get_aft, _set_aft)


  _pyangbind_elements = {'aft': aft, }


import aft
class afts(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/afts. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: The abstract forwarding tables (AFTs) that are associated
with the network instance. An AFT is instantiated per-protocol
running within the network-instance - such that one exists for
IPv4 Unicast, IPv6 Unicast, MPLS, L2 forwarding entries, etc.
A forwarding entry within the FIB has a set of next-hops,
which may be a reference to an entry within another table -
e.g., where a Layer 3 next-hop has an associated Layer 2
forwarding entry.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__aft',)

  _yang_name = 'afts'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__aft = YANGDynClass(base=YANGListType("address_family",aft.aft, yang_name="aft", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='address-family', extensions=None), is_container='list', yang_name="aft", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)

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
      return [u'network-instances', u'network-instance', u'afts']

  def _get_aft(self):
    """
    Getter method for aft, mapped from YANG variable /network_instances/network_instance/afts/aft (list)

    YANG Description: An individual abstract forwarding table associated with a
an address family wtihin the network instance.
    """
    return self.__aft
      
  def _set_aft(self, v, load=False):
    """
    Setter method for aft, mapped from YANG variable /network_instances/network_instance/afts/aft (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_aft is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_aft() directly.

    YANG Description: An individual abstract forwarding table associated with a
an address family wtihin the network instance.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("address_family",aft.aft, yang_name="aft", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='address-family', extensions=None), is_container='list', yang_name="aft", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """aft must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("address_family",aft.aft, yang_name="aft", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='address-family', extensions=None), is_container='list', yang_name="aft", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)""",
        })

    self.__aft = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_aft(self):
    self.__aft = YANGDynClass(base=YANGListType("address_family",aft.aft, yang_name="aft", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='address-family', extensions=None), is_container='list', yang_name="aft", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=True)

  aft = __builtin__.property(_get_aft, _set_aft)


  _pyangbind_elements = {'aft': aft, }


