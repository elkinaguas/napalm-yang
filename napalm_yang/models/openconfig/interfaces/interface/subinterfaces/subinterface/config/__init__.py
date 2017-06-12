
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
  from YANG module openconfig-interfaces - based on the path /interfaces/interface/subinterfaces/subinterface/config. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Configurable items at the subinterface level
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__index','__name','__description','__enabled',)

  _yang_name = 'config'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__index = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(0), is_leaf=True, yang_name="index", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces', defining_module='openconfig-interfaces', yang_type='uint32', is_config=True)
    self.__enabled = YANGDynClass(base=YANGBool, default=YANGBool("true"), is_leaf=True, yang_name="enabled", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces', defining_module='openconfig-interfaces', yang_type='boolean', is_config=True)
    self.__name = YANGDynClass(base=unicode, is_leaf=True, yang_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces', defining_module='openconfig-interfaces', yang_type='string', is_config=True)
    self.__description = YANGDynClass(base=unicode, is_leaf=True, yang_name="description", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces', defining_module='openconfig-interfaces', yang_type='string', is_config=True)

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
      return [u'interfaces', u'interface', u'subinterfaces', u'subinterface', u'config']

  def _get_index(self):
    """
    Getter method for index, mapped from YANG variable /interfaces/interface/subinterfaces/subinterface/config/index (uint32)

    YANG Description: The index of the subinterface, or logical interface number.
On systems with no support for subinterfaces, or not using
subinterfaces, this value should default to 0, i.e., the
default subinterface.
    """
    return self.__index
      
  def _set_index(self, v, load=False):
    """
    Setter method for index, mapped from YANG variable /interfaces/interface/subinterfaces/subinterface/config/index (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_index is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_index() directly.

    YANG Description: The index of the subinterface, or logical interface number.
On systems with no support for subinterfaces, or not using
subinterfaces, this value should default to 0, i.e., the
default subinterface.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(0), is_leaf=True, yang_name="index", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces', defining_module='openconfig-interfaces', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """index must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(0), is_leaf=True, yang_name="index", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces', defining_module='openconfig-interfaces', yang_type='uint32', is_config=True)""",
        })

    self.__index = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_index(self):
    self.__index = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(0), is_leaf=True, yang_name="index", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces', defining_module='openconfig-interfaces', yang_type='uint32', is_config=True)


  def _get_name(self):
    """
    Getter method for name, mapped from YANG variable /interfaces/interface/subinterfaces/subinterface/config/name (string)

    YANG Description: [adapted from IETF interfaces model (RFC 7223)]

The name of the interface.

A device MAY restrict the allowed values for this leaf,
possibly depending on the type of the interface.
For system-controlled interfaces, this leaf is the
device-specific name of the interface.  The 'config false'
list interfaces/interface[name]/state contains the currently
existing interfaces on the device.

If a client tries to create configuration for a
system-controlled interface that is not present in the
corresponding state list, the server MAY reject
the request if the implementation does not support
pre-provisioning of interfaces or if the name refers to
an interface that can never exist in the system.  A
NETCONF server MUST reply with an rpc-error with the
error-tag 'invalid-value' in this case.

The IETF model in RFC 7223 provides YANG features for the
following (i.e., pre-provisioning and arbitrary-names),
however they are omitted here:

 If the device supports pre-provisioning of interface
 configuration, the 'pre-provisioning' feature is
 advertised.

 If the device allows arbitrarily named user-controlled
 interfaces, the 'arbitrary-names' feature is advertised.

When a configured user-controlled interface is created by
the system, it is instantiated with the same name in the
/interfaces/interface[name]/state list.
    """
    return self.__name
      
  def _set_name(self, v, load=False):
    """
    Setter method for name, mapped from YANG variable /interfaces/interface/subinterfaces/subinterface/config/name (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_name() directly.

    YANG Description: [adapted from IETF interfaces model (RFC 7223)]

The name of the interface.

A device MAY restrict the allowed values for this leaf,
possibly depending on the type of the interface.
For system-controlled interfaces, this leaf is the
device-specific name of the interface.  The 'config false'
list interfaces/interface[name]/state contains the currently
existing interfaces on the device.

If a client tries to create configuration for a
system-controlled interface that is not present in the
corresponding state list, the server MAY reject
the request if the implementation does not support
pre-provisioning of interfaces or if the name refers to
an interface that can never exist in the system.  A
NETCONF server MUST reply with an rpc-error with the
error-tag 'invalid-value' in this case.

The IETF model in RFC 7223 provides YANG features for the
following (i.e., pre-provisioning and arbitrary-names),
however they are omitted here:

 If the device supports pre-provisioning of interface
 configuration, the 'pre-provisioning' feature is
 advertised.

 If the device allows arbitrarily named user-controlled
 interfaces, the 'arbitrary-names' feature is advertised.

When a configured user-controlled interface is created by
the system, it is instantiated with the same name in the
/interfaces/interface[name]/state list.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces', defining_module='openconfig-interfaces', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """name must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces', defining_module='openconfig-interfaces', yang_type='string', is_config=True)""",
        })

    self.__name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_name(self):
    self.__name = YANGDynClass(base=unicode, is_leaf=True, yang_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces', defining_module='openconfig-interfaces', yang_type='string', is_config=True)


  def _get_description(self):
    """
    Getter method for description, mapped from YANG variable /interfaces/interface/subinterfaces/subinterface/config/description (string)

    YANG Description: [adapted from IETF interfaces model (RFC 7223)]

A textual description of the interface.

A server implementation MAY map this leaf to the ifAlias
MIB object.  Such an implementation needs to use some
mechanism to handle the differences in size and characters
allowed between this leaf and ifAlias.  The definition of
such a mechanism is outside the scope of this document.

Since ifAlias is defined to be stored in non-volatile
storage, the MIB implementation MUST map ifAlias to the
value of 'description' in the persistently stored
datastore.

Specifically, if the device supports ':startup', when
ifAlias is read the device MUST return the value of
'description' in the 'startup' datastore, and when it is
written, it MUST be written to the 'running' and 'startup'
datastores.  Note that it is up to the implementation to

decide whether to modify this single leaf in 'startup' or
perform an implicit copy-config from 'running' to
'startup'.

If the device does not support ':startup', ifAlias MUST
be mapped to the 'description' leaf in the 'running'
datastore.
    """
    return self.__description
      
  def _set_description(self, v, load=False):
    """
    Setter method for description, mapped from YANG variable /interfaces/interface/subinterfaces/subinterface/config/description (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_description is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_description() directly.

    YANG Description: [adapted from IETF interfaces model (RFC 7223)]

A textual description of the interface.

A server implementation MAY map this leaf to the ifAlias
MIB object.  Such an implementation needs to use some
mechanism to handle the differences in size and characters
allowed between this leaf and ifAlias.  The definition of
such a mechanism is outside the scope of this document.

Since ifAlias is defined to be stored in non-volatile
storage, the MIB implementation MUST map ifAlias to the
value of 'description' in the persistently stored
datastore.

Specifically, if the device supports ':startup', when
ifAlias is read the device MUST return the value of
'description' in the 'startup' datastore, and when it is
written, it MUST be written to the 'running' and 'startup'
datastores.  Note that it is up to the implementation to

decide whether to modify this single leaf in 'startup' or
perform an implicit copy-config from 'running' to
'startup'.

If the device does not support ':startup', ifAlias MUST
be mapped to the 'description' leaf in the 'running'
datastore.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="description", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces', defining_module='openconfig-interfaces', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """description must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="description", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces', defining_module='openconfig-interfaces', yang_type='string', is_config=True)""",
        })

    self.__description = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_description(self):
    self.__description = YANGDynClass(base=unicode, is_leaf=True, yang_name="description", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces', defining_module='openconfig-interfaces', yang_type='string', is_config=True)


  def _get_enabled(self):
    """
    Getter method for enabled, mapped from YANG variable /interfaces/interface/subinterfaces/subinterface/config/enabled (boolean)

    YANG Description: [adapted from IETF interfaces model (RFC 7223)]

This leaf contains the configured, desired state of the
interface.

Systems that implement the IF-MIB use the value of this
leaf in the 'running' datastore to set
IF-MIB.ifAdminStatus to 'up' or 'down' after an ifEntry
has been initialized, as described in RFC 2863.

Changes in this leaf in the 'running' datastore are
reflected in ifAdminStatus, but if ifAdminStatus is
changed over SNMP, this leaf is not affected.
    """
    return self.__enabled
      
  def _set_enabled(self, v, load=False):
    """
    Setter method for enabled, mapped from YANG variable /interfaces/interface/subinterfaces/subinterface/config/enabled (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_enabled is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_enabled() directly.

    YANG Description: [adapted from IETF interfaces model (RFC 7223)]

This leaf contains the configured, desired state of the
interface.

Systems that implement the IF-MIB use the value of this
leaf in the 'running' datastore to set
IF-MIB.ifAdminStatus to 'up' or 'down' after an ifEntry
has been initialized, as described in RFC 2863.

Changes in this leaf in the 'running' datastore are
reflected in ifAdminStatus, but if ifAdminStatus is
changed over SNMP, this leaf is not affected.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, default=YANGBool("true"), is_leaf=True, yang_name="enabled", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces', defining_module='openconfig-interfaces', yang_type='boolean', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """enabled must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, default=YANGBool("true"), is_leaf=True, yang_name="enabled", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces', defining_module='openconfig-interfaces', yang_type='boolean', is_config=True)""",
        })

    self.__enabled = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_enabled(self):
    self.__enabled = YANGDynClass(base=YANGBool, default=YANGBool("true"), is_leaf=True, yang_name="enabled", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces', defining_module='openconfig-interfaces', yang_type='boolean', is_config=True)

  index = __builtin__.property(_get_index, _set_index)
  name = __builtin__.property(_get_name, _set_name)
  description = __builtin__.property(_get_description, _set_description)
  enabled = __builtin__.property(_get_enabled, _set_enabled)


  _pyangbind_elements = {'index': index, 'name': name, 'description': description, 'enabled': enabled, }


