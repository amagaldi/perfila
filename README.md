Anaconda install
==================


```
    conda install mysql-connector-python
```

## MySQL Store Procedures

### (RHI) get_boundary_layer_altitude(start date, end date)

Obtains the altitude in meters (with respect to the LIDAR) of the **Mixing Layer** and the **Residual Layer**. <br>
# Time, ID, ScanID, LOSID, Azimuth, Elevation, Range, RWS, DRWS, CNR. <br>
**Output:** Time, ID, ScanID, LID, Azimuth, Elevation, Residual Layer Altitude (m), Mixing Layer Altitude (m) <br>
Example of use:

```
call lidar.get_boundary_layer_altitude('2017-04-26 12:00:00','2017-04-29 13:00:00')
```

### (PPI) get_radial_wind_data(start date, end date)

Obtains the **Radial Wind Speed** (RWS) the **Deviation** (TODO) (DRWS) and the **Carrier to Noise Ratio** (CNR).

```
call lidar.get_radial_wind_data('2017-04-26 12:00:00','2017-04-29 13:00:00')
```
<!--
<img src="imgreadme/RWS.png" width="700px"/>  )
-->

### (DBS) get_reconstruction_wind_data(start date, end date)
Obtains the X,Y,Z components of the wind. It also has the **Carrier to Noise Ratio** (CNR) and **Confidence Index** in percentage.

```
call lidar.get_reconstruction_wind_data('2017-04-26 12:00:00','2017-04-29 13:00:00')
```
<!--
<img src="imgreadme/RWS.png" width="700px"/>  )
-->



### get_radial_absolute_beta(start date, end date)

TODO It returns a column with name 'Attenuated Absolute Beta' not sure what it is.

```
call lidar.get_radial_absolute_beta('2017-04-26 12:00:00','2017-04-26 13:00:00')

```
### get_radial_beta(start date, end date)

TODO It returns a column with name 'Attenuated Relative Beta' not sure what it is.

```
call lidar.get_radial_beta('2017-04-26 12:00:00','2017-04-26 13:00:00')
```


### get_environmental_data(start date, end date)

Obtains Information about environmental data inside and outside the LIDAR every half an hour. For example: lat, lon, internal temperature,
external temperature, external pressure, pith, roll, disk occupation, etc. 

```
call lidar.get_environmental_data('2017-04-26 12:00:00','2017-04-26 13:00:00')
```

## Glossary

**Azimuth**: Rotation in the horizontal plane (from -180 to 180).
**Elevation**: Rotation in the vertical plane (from 0 to 90).

**Mixing Layer**: The atmospheric mixed layer is defined as a layer of (approximately) constant potential temperature, or a layer in 
which the temperature falls at a rate of approximately 10 C/km, provided it is free of clouds

**Residual Layer**: 
