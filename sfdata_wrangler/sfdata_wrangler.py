__author__      = "Gregory D. Erhardt"
__copyright__   = "Copyright 2013 SFCTA"
__license__     = """
    This file is part of sfdata_wrangler.

    sfdata_wrangler is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    sfdata_wrangler is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with sfdata_wrangler.  If not, see <http://www.gnu.org/licenses/>.
"""

import datetime

from SFMuniDataHelper import SFMuniDataHelper
from GTFSHelper import GTFSHelper


def processSFMuniData(outfile, aggfile, routeEquivFile):
    """
    Reads text files containing SFMuni AVL/APC data and converts them to a 
    processed and aggregated HDF file.           
    
    outfile - HDF file containing processed disaggregate data
    aggfile - HDF file containing processed aggregate data   
    routeEquivFile - CSV file containing equivalency between AVL route IDs
                     and GTFS route IDs.                  
    """

    
    startTime = datetime.datetime.now()   
    print 'Started processing SFMuni data at ', startTime
    sfmuniHelper = SFMuniDataHelper(routeEquivFile)

    # convert the data
    #sfmuniHelper.processRawData("C:/CASA/Data/MUNI/SFMTA Data/Raw STP Files/0803.stp", outfile)
    sfmuniHelper.processRawData("C:/CASA/Data/MUNI/SFMTA Data/Raw STP Files/0906.stp", outfile)
    #sfmuniHelper.processRawData("C:/CASA/Data/MUNI/SFMTA Data/Raw STP Files/0912.stp", outfile)
    #sfmuniHelper.processRawData("C:/CASA/Data/MUNI/SFMTA Data/Raw STP Files/1001.stp", outfile)
    #sfmuniHelper.processRawData("C:/CASA/Data/MUNI/SFMTA Data/Raw STP Files/1005.stp", outfile)
    #sfmuniHelper.processRawData("C:/CASA/Data/MUNI/SFMTA Data/Raw STP Files/1009.stp", outfile)
    #sfmuniHelper.processRawData("C:/CASA/Data/MUNI/SFMTA Data/Raw STP Files/1101.stp", outfile)
    #sfmuniHelper.processRawData("C:/CASA/Data/MUNI/SFMTA Data/Raw STP Files/1110.stp", outfile)    
    #sfmuniHelper.processRawData("C:/CASA/Data/MUNI/SFMTA Data/Raw STP Files/1201.stp", outfile)
    #sfmuniHelper.processRawData("C:/CASA/Data/MUNI/SFMTA Data/Raw STP Files/1203.stp", outfile)
    #sfmuniHelper.processRawData("C:/CASA/Data/MUNI/SFMTA Data/Raw STP Files/1206.stp", outfile)
    #sfmuniHelper.processRawData("C:/CASA/Data/MUNI/SFMTA Data/Raw STP Files/1209.stp", outfile)
    #sfmuniHelper.processRawData("C:/CASA/Data/MUNI/SFMTA Data/Raw STP Files/1212.stp", outfile)
    #sfmuniHelper.processRawData("C:/CASA/Data/MUNI/SFMTA Data/Raw STP Files/1303.stp", outfile)
    #sfmuniHelper.processRawData("C:/CASA/Data/MUNI/SFMTA Data/Raw STP Files/1304.stp", outfile)
    #sfmuniHelper.processRawData("C:/CASA/Data/MUNI/SFMTA Data/Raw STP Files/1306.stp", outfile)
    #sfmuniHelper.processRawData("C:/CASA/Data/MUNI/SFMTA Data/Raw STP Files/1308.stp", outfile)
    #sfmuniHelper.processRawData("C:/CASA/Data/MUNI/SFMTA Data/Raw STP Files/1310.stp", outfile)
        
    convertedTime = datetime.datetime.now() 
    print 'Finished converting SFMuni data in ', (convertedTime - startTime)
    
    # calculate monthly averages
    #sfmuniHelper.calcMonthlyAverages(outfile, aggfile, 'sample', 'average')

    # aggregate trips into daily totals        
    #sfmuniHelper.calculateRouteStopTotals(aggfile, 'average',  'route_stops')

    # sum route totals
    #sfmuniHelper.calculateRouteTotals(aggfile, 'route_stops',  'routes')     
    
    # sum stop totals    
    #sfmuniHelper.calculateStopTotals(aggfile, 'route_stops',  'stops')
    
    # sum system totals    
    #sfmuniHelper.calculateSystemTotals(aggfile, 'route_stops',  'system')
        
    aggregatedTime = datetime.datetime.now()
    print 'Finished aggregating SFMuni data in ', (aggregatedTime - convertedTime) 


def processGTFS(outfile):
    """
    Reads files containing SFMuni General Transit Feed Specification, and converts
    them to schedule format for joining to AVL/APC data.           
    
    outfile - HDF file containing processed GTFS data             
    """

    startTime = datetime.datetime.now()   
    print 'Started processing GTFS at ', startTime
    gtfsHelper = GTFSHelper()

    # convert the data
    gtfsHelper.processRawData("C:/CASA/Data/MUNI/GTFS/san-francisco-municipal-transportation-agency_20091106_0310.zip", outfile)
        
    convertedTime = datetime.datetime.now() 
    print 'Finished converting GTFS in ', (convertedTime - startTime)
    


if __name__ == "__main__":
    
    # eventually convert filenames to arguments
    route_equiv = "C:/CASA/Data/MUNI/routeEquiv.csv"
    
    sfmuni_outfile = "C:/CASA/DataExploration/sfmuni.h5"
    sfmuni_aggfile = "C:/CASA/DataExploration/sfmuni_aggregate.h5"
    
    gtfs_outfile = "C:/CASA/DataExploration/gtfs.h5"

    processSFMuniData(sfmuni_outfile, sfmuni_aggfile, route_equiv)
    #processGTFS(gtfs_outfile)

