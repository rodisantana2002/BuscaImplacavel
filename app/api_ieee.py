import xploreapi

query = xploreapi.XPLORE('pq3rrj62ba8297n2r4mrafp6')
query.doi('10.1109/SIEDS.2011.5876877')
data = query.callAPI()
print data