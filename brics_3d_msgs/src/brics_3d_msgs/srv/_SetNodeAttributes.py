"""autogenerated by genmsg_py from SetNodeAttributesRequest.msg. Do not edit."""
import roslib.message
import struct

import brics_3d_msgs.msg

class SetNodeAttributesRequest(roslib.message.Message):
  _md5sum = "ebe4aa898f418e5ac4f34c883768f6f5"
  _type = "brics_3d_msgs/SetNodeAttributesRequest"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """
uint32 id
Attribute[] newAttributes

================================================================================
MSG: brics_3d_msgs/Attribute
# Attribute description for objects in the world model
string key
string value
"""
  __slots__ = ['id','newAttributes']
  _slot_types = ['uint32','brics_3d_msgs/Attribute[]']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.
    
    The available fields are:
       id,newAttributes
    
    @param args: complete set of field values, in .msg order
    @param kwds: use keyword arguments corresponding to message field names
    to set specific fields. 
    """
    if args or kwds:
      super(SetNodeAttributesRequest, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.id is None:
        self.id = 0
      if self.newAttributes is None:
        self.newAttributes = []
    else:
      self.id = 0
      self.newAttributes = []

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    @param buff: buffer
    @type  buff: StringIO
    """
    try:
      buff.write(_struct_I.pack(self.id))
      length = len(self.newAttributes)
      buff.write(_struct_I.pack(length))
      for val1 in self.newAttributes:
        _x = val1.key
        length = len(_x)
        buff.write(struct.pack('<I%ss'%length, length, _x))
        _x = val1.value
        length = len(_x)
        buff.write(struct.pack('<I%ss'%length, length, _x))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    @param str: byte array of serialized message
    @type  str: str
    """
    try:
      end = 0
      start = end
      end += 4
      (self.id,) = _struct_I.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.newAttributes = []
      for i in range(0, length):
        val1 = brics_3d_msgs.msg.Attribute()
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        val1.key = str[start:end]
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        val1.value = str[start:end]
        self.newAttributes.append(val1)
      return self
    except struct.error as e:
      raise roslib.message.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    @param buff: buffer
    @type  buff: StringIO
    @param numpy: numpy python module
    @type  numpy module
    """
    try:
      buff.write(_struct_I.pack(self.id))
      length = len(self.newAttributes)
      buff.write(_struct_I.pack(length))
      for val1 in self.newAttributes:
        _x = val1.key
        length = len(_x)
        buff.write(struct.pack('<I%ss'%length, length, _x))
        _x = val1.value
        length = len(_x)
        buff.write(struct.pack('<I%ss'%length, length, _x))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    @param str: byte array of serialized message
    @type  str: str
    @param numpy: numpy python module
    @type  numpy: module
    """
    try:
      end = 0
      start = end
      end += 4
      (self.id,) = _struct_I.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.newAttributes = []
      for i in range(0, length):
        val1 = brics_3d_msgs.msg.Attribute()
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        val1.key = str[start:end]
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        val1.value = str[start:end]
        self.newAttributes.append(val1)
      return self
    except struct.error as e:
      raise roslib.message.DeserializationError(e) #most likely buffer underfill

_struct_I = roslib.message.struct_I
"""autogenerated by genmsg_py from SetNodeAttributesResponse.msg. Do not edit."""
import roslib.message
import struct


class SetNodeAttributesResponse(roslib.message.Message):
  _md5sum = "95e696a0d10686913abb262e0b4cbbcf"
  _type = "brics_3d_msgs/SetNodeAttributesResponse"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """bool succeeded


"""
  __slots__ = ['succeeded']
  _slot_types = ['bool']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.
    
    The available fields are:
       succeeded
    
    @param args: complete set of field values, in .msg order
    @param kwds: use keyword arguments corresponding to message field names
    to set specific fields. 
    """
    if args or kwds:
      super(SetNodeAttributesResponse, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.succeeded is None:
        self.succeeded = False
    else:
      self.succeeded = False

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    @param buff: buffer
    @type  buff: StringIO
    """
    try:
      buff.write(_struct_B.pack(self.succeeded))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    @param str: byte array of serialized message
    @type  str: str
    """
    try:
      end = 0
      start = end
      end += 1
      (self.succeeded,) = _struct_B.unpack(str[start:end])
      self.succeeded = bool(self.succeeded)
      return self
    except struct.error as e:
      raise roslib.message.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    @param buff: buffer
    @type  buff: StringIO
    @param numpy: numpy python module
    @type  numpy module
    """
    try:
      buff.write(_struct_B.pack(self.succeeded))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    @param str: byte array of serialized message
    @type  str: str
    @param numpy: numpy python module
    @type  numpy: module
    """
    try:
      end = 0
      start = end
      end += 1
      (self.succeeded,) = _struct_B.unpack(str[start:end])
      self.succeeded = bool(self.succeeded)
      return self
    except struct.error as e:
      raise roslib.message.DeserializationError(e) #most likely buffer underfill

_struct_I = roslib.message.struct_I
_struct_B = struct.Struct("<B")
class SetNodeAttributes(roslib.message.ServiceDefinition):
  _type          = 'brics_3d_msgs/SetNodeAttributes'
  _md5sum = 'd7e195966f9a7bf1973e8543e74c46d4'
  _request_class  = SetNodeAttributesRequest
  _response_class = SetNodeAttributesResponse