from astropy.coordinates import EarthLocation
import astropy.units as u
from astroplan import Observer
from astropy.coordinates import SkyCoord
from astroplan import FixedTarget
from astropy.time import Time


#location = EarthLocation.from_geodetic(-30.83*u.deg, 21.33*u.deg)======== stupid error of mixing longitude and latitude up!
#mkat=Observer(location=location,name='MeerKAT')

#location = EarthLocation.from_geodetic(21.33*u.deg, -30.83*u.deg)


#location = EarthLocation.from_geodetic(148.2621*u.deg, -32.9986*u.deg)

location = EarthLocation.from_geodetic(21.4427901006924*u.deg, -30.83*u.deg, 1309*u.m)

#pks=Observer(location=location,name='parkes')   # done to cross-check with Parkes rise-set calculator

mkat=Observer(location=location,name='MeerKAT',timezone="Africa/Johannesburg")

coordinates = SkyCoord('13h04m39.07s','-66d43m39.7s', frame='icrs') # input YOUR source coordinates
s = FixedTarget(name='2026', coord=coordinates)
#time = Time('2022-06-17 00:00:00')

#check with parkes
'''g=pks.target_meridian_transit_time(time, s)
g1=pks.target_set_time(time, s,horizon=30.25*u.deg)
g2=pks.target_rise_time(time, s,horizon=30.25*u.deg)'''

g=mkat.target_meridian_transit_time(time, s)
g1=mkat.target_set_time(time, s,which='next',horizon=45*u.deg)  #conservative horizon given here for my purpose, mkat horizon is actually at 15 degree elevation.. you can play around with this
#g2=mkat.target_rise_time(time, s,which='previous',horizon=45*u.deg)
g2=mkat.target_rise_time(time, s,which='next',horizon=45*u.deg)
print( 'set time ' "ISO: {0.iso}, JD: {0.jd}".format(g1))
print( 'rise time ' "ISO: {0.iso}, JD: {0.jd}".format(g2))
print( 'transit time ' "ISO: {0.iso}, JD: {0.jd}".format(g))
print('MSGPS-L-2026 horizon elev45')
print('13h02m13.30s','-63h44m59.4s') # replace with YOUR source coordinates

