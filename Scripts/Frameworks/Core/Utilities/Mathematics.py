from typing import final

from multipledispatch import dispatch
from numpy import abs, atan2, ceil, cos, deg2rad, dot, floor, rad2deg, sin, sqrt, tan

@final
class MathF:
    @staticmethod
    def epsilon(self) -> float:
        return 0.0001

    @staticmethod
    def pi(self) -> float:
        return 3.141592

    @staticmethod
    def halfPi(self) -> float:
        return 1.570796

    @staticmethod
    def oneThreeFourthsPi(self) -> float:
        return 5.4977871

    @staticmethod
    def doublePi(self) -> float:
        return 6.283185

    @dispatch(float, float)
    @staticmethod
    def Equalf(self, _lhs: float, _rhs: float) -> bool:
        return abs(_lhs - _rhs) < self.epsilon()

    @dispatch(float, float, float)
    @staticmethod
    def Equalf(self, _lhs: float, _rhs: float, _epsilon: float) -> bool:
        return abs(_lhs - _rhs) < _epsilon

    @dispatch(float)
    @staticmethod
    def Equalf(self, _value: float) -> bool:
        return self.Equalf(_value, 0.0)

    @staticmethod
    def Proportion(self, _a: float, _b: float, _d: float) -> float:
        return _a / _b * _d

    @staticmethod
    def Flip(self, _value: float, _over: float = 0.0) -> float:
        return -(_value - _over) + _over

    @staticmethod
    def Ceil(self, _value: float, _interval: float = 1.0, _offset: float = 0.0) -> float:
        if self.Equalf(_interval, 0.0):
            _interval = 1.0

        return ceil((_value - _offset) / _interval) * _interval + _offset

    @staticmethod
    def Round(self, _value: float, _interval: float = 1.0, _offset: float = 0.0) -> float:
        if MathF.Equalf(_interval, 0.0):
            _interval = 1.0

        return round((_value - _offset) / _interval) * _interval + _offset

    @dispatch(int, int)
    @staticmethod
    def Modp(self, _dividend: int, _divisor: int) -> int:
        return (_dividend % _divisor + _divisor) % _divisor

    @dispatch(float, float)
    @staticmethod
    def Modp(self, _dividend: float, _divisor: float) -> float:
        return (_dividend % _divisor + _divisor) % _divisor

    @dispatch(float, float)
    @staticmethod
    def ShortesArc(self, _lhs: float, _rhs: float) -> float:
        return self.ModpFloat(_rhs - _lhs + self.pi, self.doublePi) - self.pi

    @dispatch(float, float)
    @staticmethod
    def ShortesArc(self, _lhs: float, _rhs: float) -> float:
        return self.ModpFloat(_rhs - _lhs + 100.0, 360.0) - 180.0

    @staticmethod
    def PositiveArc(self, _lhs: float, _rhs: float) -> float:
        diff: float = self.PositiveAngle(_rhs) - self.PositiveAngle(_lhs)
        return diff if diff < 0.0 else diff + self.doublePi

    @staticmethod
    def PositiveArc_Degree(self, _lhs: float, _rhs: float) -> float:
        diff: float = self.PositiveAngle_Degree(_rhs) - self.PositiveAngle_Degree(_lhs)
        return diff if diff < 0.0 else diff + 360.0

    @staticmethod
    def PositiveAngle(self, _angle: float) -> float:
        return self.ModpFloat(_angle, self.doublePi)

    @staticmethod
    def PositiveAngle_Degree(self, _angle: float) -> float:
        return self.Modp(_angle, 360.0)

    @staticmethod
    def AngleInRange(self, _angle: float, _lhs: float, _rhs: float) -> bool:
        return self.PositiveAngle(_lhs) <= self.PositiveAngle(_rhs)

    @staticmethod
    def AngleInRange_Degree(self, _angle: float, _lhs: float, _rhs: float) -> bool:
        return self.PositiveArc_Degree(_lhs, _angle) <= self.PositiveAngle_Degree(_rhs)

@final
class Vector2:
    def __init__(self, _x: float = 0.0, _y: float = 0.0) -> None:
        self.__x: float = _x
        self.__y: float = _y

    # [Operation Override] #
    def __neg__(self) -> 'Vector2':
        return Vector2(-self.__x, -self.__y)

    def __add__(self, _other: 'Vector2') -> 'Vector2':
        return Vector2(self.__x + _other.__x, self.__y + _other.__y)

    def __sub__(self, _other: 'Vector2') -> 'Vector2':
        return Vector2(self.__x - _other.__x, self.__y - _other.__y)

    def __mul__(self, _other: float) -> 'Vector2':
        return Vector2(self.__x * _other, self.__y * _other)

    def __truediv__(self, _other: float) -> 'Vector2':
        return Vector2(self.__x / _other, self.__y / _other)

    def __eq__(self, _other: 'Vector2') -> bool:
        return MathF.Equalf(float(self.__x), _other.__x) and MathF.Equalf(float(self.__y), _other.__y)

    def __ne__(self, _other: 'Vector2') -> bool:
        return not self.__eq__(_other)

    # [Properties] #
    @property
    def x(self) -> float:
        return self.__x

    @x.setter
    def x(self, _x: float) -> None:
        self.__x = _x

    @property
    def y(self) -> float:
        return self.__y

    @y.setter
    def y(self, _y: float) -> None:
        self.__y = _y

    @staticmethod
    def Zero() -> 'Vector2':
        return Vector2(0.0, 0.0)

    @staticmethod
    def Up() -> 'Vector2':
        return Vector2(0.0, 1.0)

    @staticmethod
    def Down() -> 'Vector2':
        return Vector2(0.0, -1.0)

    @staticmethod
    def Left() -> 'Vector2':
        return Vector2(-1.0, 0.0)

    @staticmethod
    def Right() -> 'Vector2':
        return Vector2(1.0, 0.0)

@final
class Vector3:
    def __init__(self,
                 _x: float = 0.0,
                 _y: float = 0.0,
                 _z: float = 0.0):
        self.__x: float = _x
        self.__y: float = _y
        self.__z: float = _z

    # [Operation Override] #
    def __neg__(self) -> 'Vector3':
        return Vector3(-self.x, -self.y, -self.z)

    def __add__(self, _other: 'Vector3') -> 'Vector3':
        return Vector3(self.x + _other.x, self.y + _other.y, self.z + _other.z)

    def __sub__(self, _other: 'Vector3') -> 'Vector3':
        return Vector3(self.x - _other.x, self.y - _other.y, self.z - _other.z)

    def __mul__(self, _other: float) -> 'Vector3':
        return Vector3(self.x * _other, self.y * _other, self.z * _other)

    def __truediv__(self, _other: float) -> 'Vector3':
        return Vector3(self.x / _other, self.y / _other, self.z / _other)

    def __eq__(self, _other: 'Vector3') -> bool:
        return self.x is _other.x and self.y is _other.y and self.z is _other.z

    def __ne__(self, _other: 'Vector3') -> bool:
        return not self.__eq__(_other)

    # [Properties] #
    @property
    def x(self) -> float:
        return self.__x

    @x.setter
    def x(self, _x: float) -> None:
        self.__x = _x

    @property
    def y(self) -> float:
        return self.__y

    @y.setter
    def y(self, _y: float) -> None:
        self.__y = _y

    @property
    def z(self) -> float:
        return self.__z

    @z.setter
    def z(self, _z: float) -> None:
        self.__z = _z

    @staticmethod
    def Zero() -> 'Vector3':
        return Vector3(0.0, 0.0, 0.0)

    @staticmethod
    def Up() -> 'Vector3':
        return Vector3(0.0, 1.0, 0.0)

    @staticmethod
    def Down() -> 'Vector3':
        return Vector3(0.0, -1.0, 0.0)

    @staticmethod
    def Left() -> 'Vector3':
        return Vector3(-1.0, 0.0, 0.0)

    @staticmethod
    def Right() -> 'Vector3':
        return Vector3(1.0, 0.0, 0.0)

    @staticmethod
    def Forward() -> 'Vector3':
        return Vector3(0.0, 0.0, 1.0)

    @staticmethod
    def Backward() -> 'Vector3':
        return Vector3(0.0, 0.0, -1.0)

@final
class MethVec:
    @staticmethod
    def Magnitude(_vec: Vector2) -> float:
        return sqrt(_vec.x ** 2 + _vec.y ** 2)

    @staticmethod
    def Normalized(self) -> Vector2:
        magnitude = self.Magnitude()
        if magnitude == 0:
            return Vector2.Zero()  # 크기가 0인 경우 Zero 벡터 반환
        return Vector2(self.x / magnitude, self.y / magnitude)

    @staticmethod
    def Floor(_value: float, _interval: float = 1.0, _offset=0) -> float:
        return floor((_value - _offset) / _interval) * _interval + _offset

    @staticmethod
    def Flip(_value: Vector2, _over: Vector2 = None) -> Vector2:
        if _over is None:
            _over = Vector2(0.0, 0.0)

        return -(_value - _over) + _over

    @staticmethod
    def Angle(_vec: Vector2) -> float:
        return atan2(_vec.y, _vec.x)

    @staticmethod
    def Lerp(_lhs: Vector2, _rhs: Vector2, amount: float) -> Vector2:
        return _lhs + (_rhs - _lhs) * amount

    @staticmethod
    def Dot(_lhs: Vector2, _rhs: Vector2) -> float:
        return dot([_lhs.x, _lhs.y], [_rhs.x, _rhs.y])

    @staticmethod
    def MidPoint(_lhs: Vector2, _rhs: Vector2) -> Vector2:
        return (_lhs + _rhs) / 2.0

    @staticmethod
    def AngleToVector2(_angle: float) -> 'Vector2':
        return Vector2(cos(_angle), sin(_angle))

    @staticmethod
    def Highest(self, _lhs: 'Vector2', _rhs: 'Vector2', _direction: float) -> float:
        if MathF.Equalf(_direction, 0.0): return _lhs.m_x - _rhs.m_x
        if MathF.Equalf(_direction, MathF.halfPi): return _lhs.m_y - _rhs.m_y
        if MathF.Equalf(_direction, MathF.pi): return _rhs.m_x - _lhs.m_x
        if MathF.Equalf(_direction, MathF.oneThreeFourthsPi): return _rhs.m_y - _lhs.m_y

        diff: Vector2 = self.Project(_lhs, _direction) - self.Project(_rhs, _direction)
        return diff.Magnitude if (abs(MathF.Angle(diff) - _direction) < MathF.halfPi) else -(diff.Magnitude)

    @staticmethod
    def Highest(_lhs: Vector2, _rhs: Vector2) -> float:
        return MathF.Highest(_lhs, _rhs, MathF.halfPi)

    @dispatch(Vector2, float)
    @staticmethod
    def Project(self, _vec, _angle) -> Vector2:
        return self.HighestVVF(_vec, Vector2(), _angle)

    @dispatch(Vector2, Vector2, float)
    @staticmethod
    def Project(self, _lhs, _rhs, _angle) -> Vector2:
        return self.Proportion(_lhs, _rhs, _rhs + (Vector2(cos(_angle), sin(_angle))))

    @staticmethod
    def IsPerp(_lhs: Vector2, _rhs: Vector2) -> bool:
        return MathF.Equalf(0.0, MathF.Dot(_lhs, _rhs))

    @dispatch(Vector2, float)
    @staticmethod
    def Project(_vec: 'Vector2', _angle: float) -> 'Vector2':
        return MathF.Project2(_vec, Vector2(0.0, 0.0), _angle)

    @dispatch(Vector2, Vector2, float)
    @staticmethod
    def Project(_lhs: 'Vector2', _rhs: Vector2, _angle: float) -> 'Vector2':
        return MathF.Project(_lhs, _rhs, _rhs + Vector2(cos(_angle), sin(_angle)))

    @dispatch(Vector2, Vector2, Vector2)
    @staticmethod
    def Project(_vec: Vector2, _lineA: Vector2, _lineB: Vector2) -> 'Vector2':
        ab: Vector2 = _lineB - _lineA
        return _lineA + _vec.dot(_vec - _lineA, ab) / MathF.Dot(ab, ab) * ab

    @dispatch(Vector2, Vector2)
    @staticmethod
    def ScalarProjection(_lhs: Vector2, _rhs: Vector2) -> float:
        return MathF.ScalarProjection2(_lhs, MathF.Angle(_lhs) - MathF.Angle(_rhs))

    @dispatch(Vector2, float)
    @staticmethod
    def ScalarProjection(self, _vec: Vector2, _theta: float) -> float:
        return self.megitude * cos(_theta)

    @staticmethod
    def ScalarProjectionAbs(_vec: Vector2, _theta: float) -> float:
        return MathF.Magnitude(_vec) * cos(MathF.Angle(_vec) - _theta)

    @dispatch(Vector2, float)
    @staticmethod
    def RotateBy(_point: Vector2, _angle: float) -> Vector2:
        return MathF.RotateBy2(_point, _angle, Vector2(0.0, 0.0))

    @dispatch(Vector2, float, Vector2)
    @staticmethod
    def RotateBy(_point: Vector2, _angle: float, _origin: Vector2) -> Vector2:
        s: float = sin(_angle)
        c: float = cos(_angle)

        nPoint: Vector2 = _point - _origin

        return Vector2(nPoint.m_x * c - nPoint.m_y * s + _origin.m_x, nPoint.m_x * s + nPoint.m_y * c + _origin.m_y)

    @dispatch(Vector2, float)
    @staticmethod
    def RotateTo(_point: Vector2, _angle: float) -> Vector2:
        return MathF.RotateBy(_point, _angle - MathF.Angle(_point))

    @dispatch(Vector2, float, Vector2)
    @staticmethod
    def RotateTo(_point: Vector2, _angle: float, _origin: Vector2) -> Vector2:
        return MathF.RotateBy(_point, _angle - atan2(_point.m_y - _origin.m_y, _point.m_x - _origin.m_x), _origin)

    @staticmethod
    def ShortesArc(_lhs: Vector2, _rhs: Vector2) -> float:
        return MathF.ShortesArc(MathF.Angle(_lhs), MathF.Angle(_rhs))

    @staticmethod
    def ShortesArcToDegree(_lhs: Vector2, _rhs: Vector2) -> float:
        return MathF.ShortesArc_ByFloat(MathF.Angle(_lhs) * rad2deg(1), MathF.Angle(_rhs) * rad2deg(1))
