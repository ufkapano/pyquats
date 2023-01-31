# pyquats package

Python implementation of quaternions is presented. 

## Modules

* pyquats.quats - Quat class
* pyquats.numpyquats - Quat class using numpy (slow)
* pyquats.qmath - mathematical functions for quaternions
[sgn(q), exp(q), log(c), sin(q), cos(q), sinh(q), cosh(q)]
* pyquats.qtools - rotations, random unit quaternions

## Download

To install an official release do

    python3 -m pip install pyquats

To get the git version do

    git clone https://github.com/ufkapano/pyquats.git

## Usage

See doc/quickstart.txt

~~~python
>>> from pyquats.quats import Quat
>>> ii = Quat(0, 1)
>>> jj = Quat(0, 0, 1)
>>> kk = Quat(0, 0, 0, 1)
>>> ii * jj == kk
True
>>> ii ** 2 == jj ** 2 == kk ** 2 == -1
True
>>> all(q.is_unit() for q in (Quat(1), ii, jj, kk))
True
>>> p = Quat(5.0, 2.5, -3.6, 4.9)
>>> p.conjugate()
Quat(5.0, -2.5, 3.6, -4.9)
>>> ~p
Quat(0.0732922896511287, -0.03664614482556435, 0.052770448548812667, -0.07182644385810613)
>>> p * ~p
Quat(1.0, 0.0, -2.7755575615628914e-17, 5.551115123125783e-17)
>>> list(p)
[5.0, 2.5, -3.6, 4.9]
~~~

## Contributors

Andrzej Kapanowski (project leader)

Jan Ferdyan (quaternion functions)

## References

[1] http://en.wikipedia.org/wiki/Quaternion

[2] Real Quaternionic Calculus Handbook,
João Pedro Morais, Svetlin Georgiev, Wolfgang Sprößig,
Birkhäuser Basel 2014.

EOF
