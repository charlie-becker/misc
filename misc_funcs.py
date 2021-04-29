import scipy

def find_coord_indices(lon_array, lat_array, lon_points, lat_points):
    """
    Find indices of nearest lon/lat pair on a grid. Supports rectilinear and curilinear grids. 
    lon_points / lat_points must be a list. 
    """
    lonlat = np.column_stack((lon_array.ravel(), lat_array.ravel()))
    ll = np.array([lon_points, lat_points]).T#reshape(len(lon_points), 2)
    idx = scipy.spatial.distance.cdist(lonlat, ll).argmin(0)
    
    return np.column_stack((np.unravel_index(idx, lon_array.shape))).tolist()
  
  #############################################################################################
