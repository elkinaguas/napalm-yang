
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

import lsa_type
class lsa_types(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa-types. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Enclosing container for a list of LSA types that are
in the LSDB for the specified area
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__lsa_type',)

  _yang_name = 'lsa-types'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__lsa_type = YANGDynClass(base=YANGListType("type",lsa_type.lsa_type, yang_name="lsa-type", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='type', extensions=None), is_container='list', yang_name="lsa-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)

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
      return [u'network-instances', u'network-instance', u'protocols', u'protocol', u'ospfv2', u'areas', u'area', u'lsdb', u'lsa-types']

  def _get_lsa_type(self):
    """
    Getter method for lsa_type, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa_types/lsa_type (list)

    YANG Description: List of LSA types in the LSDB for the specified
area
    """
    return self.__lsa_type
      
  def _set_lsa_type(self, v, load=False):
    """
    Setter method for lsa_type, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa_types/lsa_type (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_lsa_type is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_lsa_type() directly.

    YANG Description: List of LSA types in the LSDB for the specified
area
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("type",lsa_type.lsa_type, yang_name="lsa-type", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='type', extensions=None), is_container='list', yang_name="lsa-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """lsa_type must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("type",lsa_type.lsa_type, yang_name="lsa-type", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='type', extensions=None), is_container='list', yang_name="lsa-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)""",
        })

    self.__lsa_type = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_lsa_type(self):
    self.__lsa_type = YANGDynClass(base=YANGListType("type",lsa_type.lsa_type, yang_name="lsa-type", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='type', extensions=None), is_container='list', yang_name="lsa-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)

  lsa_type = __builtin__.property(_get_lsa_type)


  _pyangbind_elements = {'lsa_type': lsa_type, }


import lsa_type
class lsa_types(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa-types. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Enclosing container for a list of LSA types that are
in the LSDB for the specified area
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__lsa_type',)

  _yang_name = 'lsa-types'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__lsa_type = YANGDynClass(base=YANGListType("type",lsa_type.lsa_type, yang_name="lsa-type", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='type', extensions=None), is_container='list', yang_name="lsa-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)

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
      return [u'network-instances', u'network-instance', u'protocols', u'protocol', u'ospfv2', u'areas', u'area', u'lsdb', u'lsa-types']

  def _get_lsa_type(self):
    """
    Getter method for lsa_type, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa_types/lsa_type (list)

    YANG Description: List of LSA types in the LSDB for the specified
area
    """
    return self.__lsa_type
      
  def _set_lsa_type(self, v, load=False):
    """
    Setter method for lsa_type, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa_types/lsa_type (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_lsa_type is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_lsa_type() directly.

    YANG Description: List of LSA types in the LSDB for the specified
area
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("type",lsa_type.lsa_type, yang_name="lsa-type", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='type', extensions=None), is_container='list', yang_name="lsa-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """lsa_type must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("type",lsa_type.lsa_type, yang_name="lsa-type", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='type', extensions=None), is_container='list', yang_name="lsa-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)""",
        })

    self.__lsa_type = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_lsa_type(self):
    self.__lsa_type = YANGDynClass(base=YANGListType("type",lsa_type.lsa_type, yang_name="lsa-type", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='type', extensions=None), is_container='list', yang_name="lsa-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)

  lsa_type = __builtin__.property(_get_lsa_type)


  _pyangbind_elements = {'lsa_type': lsa_type, }


