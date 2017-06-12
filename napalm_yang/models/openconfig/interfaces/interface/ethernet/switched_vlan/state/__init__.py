
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
  from YANG module openconfig-interfaces - based on the path /interfaces/interface/ethernet/switched-vlan/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: State variables for VLANs
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__interface_mode','__native_vlan','__access_vlan','__trunk_vlans',)

  _yang_name = 'state'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__native_vlan = YANGDynClass(base=[RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': [u'1..4094']}),RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(409[0-4]|40[0-8][0-9]|[1-3][0-9]{3}|[1-9][0-9]{1,2}|[1-9])\\.((409[0-4]|40[0-8][0-9]|[1-3][0-9]{3}|[1-9][0-9]{1,2}|[1-9])|\\*)'}),], is_leaf=True, yang_name="native-vlan", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/vlan', defining_module='openconfig-vlan', yang_type='union', is_config=False)
    self.__access_vlan = YANGDynClass(base=[RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': [u'1..4094']}),RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(409[0-4]|40[0-8][0-9]|[1-3][0-9]{3}|[1-9][0-9]{1,2}|[1-9])\\.((409[0-4]|40[0-8][0-9]|[1-3][0-9]{3}|[1-9][0-9]{1,2}|[1-9])|\\*)'}),], is_leaf=True, yang_name="access-vlan", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/vlan', defining_module='openconfig-vlan', yang_type='union', is_config=False)
    self.__trunk_vlans = YANGDynClass(base=TypedListType(allowed_type=[RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': [u'1..4094']}),RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(409[0-4]|40[0-8][0-9]|[1-3][0-9]{3}|[1-9][0-9]{1,2}|[1-9])\\.\\.(409[0-4]|40[0-8][0-9]|[1-3][0-9]{3}|[1-9][0-9]{1,2}|[1-9])'}),RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(409[0-4]|40[0-8][0-9]|[1-3][0-9]{3}|[1-9][0-9]{1,2}|[1-9])\\.((409[0-4]|40[0-8][0-9]|[1-3][0-9]{3}|[1-9][0-9]{1,2}|[1-9])|\\*)'}),RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(409[0-4]|40[0-8][0-9]|[1-3][0-9]{3}|[1-9][0-9]{1,2}|[1-9])\\.\\.(409[0-4]|40[0-8][0-9]|[1-3][0-9]{3}|[1-9][0-9]{1,2}|[1-9])\\.((409[0-4]|40[0-8][0-9]|[1-3][0-9]{3}|[1-9][0-9]{1,2}|[1-9])|\\*)'}),RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(\\*|(409[0-4]|40[0-8][0-9]|[1-3][0-9]{3}|[1-9][0-9]{1,2}|[1-9]))\\.(409[0-4]|40[0-8][0-9]|[1-3][0-9]{3}|[1-9][0-9]{1,2}|[1-9])\\.\\.(409[0-4]|40[0-8][0-9]|[1-3][0-9]{3}|[1-9][0-9]{1,2}|[1-9])'}),]), is_leaf=False, yang_name="trunk-vlans", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/vlan', defining_module='openconfig-vlan', yang_type='union', is_config=False)
    self.__interface_mode = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'ACCESS': {}, u'TRUNK': {}},), is_leaf=True, yang_name="interface-mode", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/vlan', defining_module='openconfig-vlan', yang_type='oc-vlan-types:vlan-mode-type', is_config=False)

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
      return [u'interfaces', u'interface', u'ethernet', u'switched-vlan', u'state']

  def _get_interface_mode(self):
    """
    Getter method for interface_mode, mapped from YANG variable /interfaces/interface/ethernet/switched_vlan/state/interface_mode (oc-vlan-types:vlan-mode-type)

    YANG Description: Set the interface to access or trunk mode for
VLANs
    """
    return self.__interface_mode
      
  def _set_interface_mode(self, v, load=False):
    """
    Setter method for interface_mode, mapped from YANG variable /interfaces/interface/ethernet/switched_vlan/state/interface_mode (oc-vlan-types:vlan-mode-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_interface_mode is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_interface_mode() directly.

    YANG Description: Set the interface to access or trunk mode for
VLANs
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'ACCESS': {}, u'TRUNK': {}},), is_leaf=True, yang_name="interface-mode", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/vlan', defining_module='openconfig-vlan', yang_type='oc-vlan-types:vlan-mode-type', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """interface_mode must be of a type compatible with oc-vlan-types:vlan-mode-type""",
          'defined-type': "oc-vlan-types:vlan-mode-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'ACCESS': {}, u'TRUNK': {}},), is_leaf=True, yang_name="interface-mode", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/vlan', defining_module='openconfig-vlan', yang_type='oc-vlan-types:vlan-mode-type', is_config=False)""",
        })

    self.__interface_mode = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_interface_mode(self):
    self.__interface_mode = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'ACCESS': {}, u'TRUNK': {}},), is_leaf=True, yang_name="interface-mode", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/vlan', defining_module='openconfig-vlan', yang_type='oc-vlan-types:vlan-mode-type', is_config=False)


  def _get_native_vlan(self):
    """
    Getter method for native_vlan, mapped from YANG variable /interfaces/interface/ethernet/switched_vlan/state/native_vlan (union)

    YANG Description: Set the native VLAN id for untagged frames arriving on
a trunk interface.  This configuration is only valid on
a trunk interface.
    """
    return self.__native_vlan
      
  def _set_native_vlan(self, v, load=False):
    """
    Setter method for native_vlan, mapped from YANG variable /interfaces/interface/ethernet/switched_vlan/state/native_vlan (union)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_native_vlan is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_native_vlan() directly.

    YANG Description: Set the native VLAN id for untagged frames arriving on
a trunk interface.  This configuration is only valid on
a trunk interface.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=[RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': [u'1..4094']}),RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(409[0-4]|40[0-8][0-9]|[1-3][0-9]{3}|[1-9][0-9]{1,2}|[1-9])\\.((409[0-4]|40[0-8][0-9]|[1-3][0-9]{3}|[1-9][0-9]{1,2}|[1-9])|\\*)'}),], is_leaf=True, yang_name="native-vlan", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/vlan', defining_module='openconfig-vlan', yang_type='union', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """native_vlan must be of a type compatible with union""",
          'defined-type': "openconfig-vlan:union",
          'generated-type': """YANGDynClass(base=[RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': [u'1..4094']}),RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(409[0-4]|40[0-8][0-9]|[1-3][0-9]{3}|[1-9][0-9]{1,2}|[1-9])\\.((409[0-4]|40[0-8][0-9]|[1-3][0-9]{3}|[1-9][0-9]{1,2}|[1-9])|\\*)'}),], is_leaf=True, yang_name="native-vlan", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/vlan', defining_module='openconfig-vlan', yang_type='union', is_config=False)""",
        })

    self.__native_vlan = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_native_vlan(self):
    self.__native_vlan = YANGDynClass(base=[RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': [u'1..4094']}),RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(409[0-4]|40[0-8][0-9]|[1-3][0-9]{3}|[1-9][0-9]{1,2}|[1-9])\\.((409[0-4]|40[0-8][0-9]|[1-3][0-9]{3}|[1-9][0-9]{1,2}|[1-9])|\\*)'}),], is_leaf=True, yang_name="native-vlan", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/vlan', defining_module='openconfig-vlan', yang_type='union', is_config=False)


  def _get_access_vlan(self):
    """
    Getter method for access_vlan, mapped from YANG variable /interfaces/interface/ethernet/switched_vlan/state/access_vlan (union)

    YANG Description: Assign the access vlan to the access port.
    """
    return self.__access_vlan
      
  def _set_access_vlan(self, v, load=False):
    """
    Setter method for access_vlan, mapped from YANG variable /interfaces/interface/ethernet/switched_vlan/state/access_vlan (union)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_access_vlan is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_access_vlan() directly.

    YANG Description: Assign the access vlan to the access port.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=[RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': [u'1..4094']}),RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(409[0-4]|40[0-8][0-9]|[1-3][0-9]{3}|[1-9][0-9]{1,2}|[1-9])\\.((409[0-4]|40[0-8][0-9]|[1-3][0-9]{3}|[1-9][0-9]{1,2}|[1-9])|\\*)'}),], is_leaf=True, yang_name="access-vlan", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/vlan', defining_module='openconfig-vlan', yang_type='union', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """access_vlan must be of a type compatible with union""",
          'defined-type': "openconfig-vlan:union",
          'generated-type': """YANGDynClass(base=[RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': [u'1..4094']}),RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(409[0-4]|40[0-8][0-9]|[1-3][0-9]{3}|[1-9][0-9]{1,2}|[1-9])\\.((409[0-4]|40[0-8][0-9]|[1-3][0-9]{3}|[1-9][0-9]{1,2}|[1-9])|\\*)'}),], is_leaf=True, yang_name="access-vlan", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/vlan', defining_module='openconfig-vlan', yang_type='union', is_config=False)""",
        })

    self.__access_vlan = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_access_vlan(self):
    self.__access_vlan = YANGDynClass(base=[RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': [u'1..4094']}),RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(409[0-4]|40[0-8][0-9]|[1-3][0-9]{3}|[1-9][0-9]{1,2}|[1-9])\\.((409[0-4]|40[0-8][0-9]|[1-3][0-9]{3}|[1-9][0-9]{1,2}|[1-9])|\\*)'}),], is_leaf=True, yang_name="access-vlan", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/vlan', defining_module='openconfig-vlan', yang_type='union', is_config=False)


  def _get_trunk_vlans(self):
    """
    Getter method for trunk_vlans, mapped from YANG variable /interfaces/interface/ethernet/switched_vlan/state/trunk_vlans (union)

    YANG Description: Specify VLANs, or ranges thereof, that the interface may
carry when in trunk mode.  If not specified, all VLANs are
allowed on the interface. Ranges are specified in the form
x..y, where x<y - ranges are assumed to be inclusive (such
that the VLAN range is x <= range <= y.
    """
    return self.__trunk_vlans
      
  def _set_trunk_vlans(self, v, load=False):
    """
    Setter method for trunk_vlans, mapped from YANG variable /interfaces/interface/ethernet/switched_vlan/state/trunk_vlans (union)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_trunk_vlans is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_trunk_vlans() directly.

    YANG Description: Specify VLANs, or ranges thereof, that the interface may
carry when in trunk mode.  If not specified, all VLANs are
allowed on the interface. Ranges are specified in the form
x..y, where x<y - ranges are assumed to be inclusive (such
that the VLAN range is x <= range <= y.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=TypedListType(allowed_type=[RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': [u'1..4094']}),RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(409[0-4]|40[0-8][0-9]|[1-3][0-9]{3}|[1-9][0-9]{1,2}|[1-9])\\.\\.(409[0-4]|40[0-8][0-9]|[1-3][0-9]{3}|[1-9][0-9]{1,2}|[1-9])'}),RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(409[0-4]|40[0-8][0-9]|[1-3][0-9]{3}|[1-9][0-9]{1,2}|[1-9])\\.((409[0-4]|40[0-8][0-9]|[1-3][0-9]{3}|[1-9][0-9]{1,2}|[1-9])|\\*)'}),RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(409[0-4]|40[0-8][0-9]|[1-3][0-9]{3}|[1-9][0-9]{1,2}|[1-9])\\.\\.(409[0-4]|40[0-8][0-9]|[1-3][0-9]{3}|[1-9][0-9]{1,2}|[1-9])\\.((409[0-4]|40[0-8][0-9]|[1-3][0-9]{3}|[1-9][0-9]{1,2}|[1-9])|\\*)'}),RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(\\*|(409[0-4]|40[0-8][0-9]|[1-3][0-9]{3}|[1-9][0-9]{1,2}|[1-9]))\\.(409[0-4]|40[0-8][0-9]|[1-3][0-9]{3}|[1-9][0-9]{1,2}|[1-9])\\.\\.(409[0-4]|40[0-8][0-9]|[1-3][0-9]{3}|[1-9][0-9]{1,2}|[1-9])'}),]), is_leaf=False, yang_name="trunk-vlans", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/vlan', defining_module='openconfig-vlan', yang_type='union', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """trunk_vlans must be of a type compatible with union""",
          'defined-type': "openconfig-vlan:union",
          'generated-type': """YANGDynClass(base=TypedListType(allowed_type=[RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': [u'1..4094']}),RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(409[0-4]|40[0-8][0-9]|[1-3][0-9]{3}|[1-9][0-9]{1,2}|[1-9])\\.\\.(409[0-4]|40[0-8][0-9]|[1-3][0-9]{3}|[1-9][0-9]{1,2}|[1-9])'}),RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(409[0-4]|40[0-8][0-9]|[1-3][0-9]{3}|[1-9][0-9]{1,2}|[1-9])\\.((409[0-4]|40[0-8][0-9]|[1-3][0-9]{3}|[1-9][0-9]{1,2}|[1-9])|\\*)'}),RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(409[0-4]|40[0-8][0-9]|[1-3][0-9]{3}|[1-9][0-9]{1,2}|[1-9])\\.\\.(409[0-4]|40[0-8][0-9]|[1-3][0-9]{3}|[1-9][0-9]{1,2}|[1-9])\\.((409[0-4]|40[0-8][0-9]|[1-3][0-9]{3}|[1-9][0-9]{1,2}|[1-9])|\\*)'}),RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(\\*|(409[0-4]|40[0-8][0-9]|[1-3][0-9]{3}|[1-9][0-9]{1,2}|[1-9]))\\.(409[0-4]|40[0-8][0-9]|[1-3][0-9]{3}|[1-9][0-9]{1,2}|[1-9])\\.\\.(409[0-4]|40[0-8][0-9]|[1-3][0-9]{3}|[1-9][0-9]{1,2}|[1-9])'}),]), is_leaf=False, yang_name="trunk-vlans", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/vlan', defining_module='openconfig-vlan', yang_type='union', is_config=False)""",
        })

    self.__trunk_vlans = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_trunk_vlans(self):
    self.__trunk_vlans = YANGDynClass(base=TypedListType(allowed_type=[RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': [u'1..4094']}),RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(409[0-4]|40[0-8][0-9]|[1-3][0-9]{3}|[1-9][0-9]{1,2}|[1-9])\\.\\.(409[0-4]|40[0-8][0-9]|[1-3][0-9]{3}|[1-9][0-9]{1,2}|[1-9])'}),RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(409[0-4]|40[0-8][0-9]|[1-3][0-9]{3}|[1-9][0-9]{1,2}|[1-9])\\.((409[0-4]|40[0-8][0-9]|[1-3][0-9]{3}|[1-9][0-9]{1,2}|[1-9])|\\*)'}),RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(409[0-4]|40[0-8][0-9]|[1-3][0-9]{3}|[1-9][0-9]{1,2}|[1-9])\\.\\.(409[0-4]|40[0-8][0-9]|[1-3][0-9]{3}|[1-9][0-9]{1,2}|[1-9])\\.((409[0-4]|40[0-8][0-9]|[1-3][0-9]{3}|[1-9][0-9]{1,2}|[1-9])|\\*)'}),RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(\\*|(409[0-4]|40[0-8][0-9]|[1-3][0-9]{3}|[1-9][0-9]{1,2}|[1-9]))\\.(409[0-4]|40[0-8][0-9]|[1-3][0-9]{3}|[1-9][0-9]{1,2}|[1-9])\\.\\.(409[0-4]|40[0-8][0-9]|[1-3][0-9]{3}|[1-9][0-9]{1,2}|[1-9])'}),]), is_leaf=False, yang_name="trunk-vlans", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/vlan', defining_module='openconfig-vlan', yang_type='union', is_config=False)

  interface_mode = __builtin__.property(_get_interface_mode)
  native_vlan = __builtin__.property(_get_native_vlan)
  access_vlan = __builtin__.property(_get_access_vlan)
  trunk_vlans = __builtin__.property(_get_trunk_vlans)


  _pyangbind_elements = {'interface_mode': interface_mode, 'native_vlan': native_vlan, 'access_vlan': access_vlan, 'trunk_vlans': trunk_vlans, }


