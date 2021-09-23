import h5py
import numpy as np
import bdv
import imglyb
import scyjava
import threading
import time

scyjava.config.endpoints.append('sc.fiji:bigdataviewer-vistools:1.0.0-beta-25')
scyjava.start_jvm()

path = '/home/hanslovskyp/Downloads/sample_A_padded_20160501.hdf'

BdvFunctions        = bdv.BdvFunctions
VolatileTypeMatcher = scyjava.jimport('bdv.util.volatiles.VolatileTypeMatcher')
VolatileViews       = scyjava.jimport('bdv.util.volatiles.VolatileViews')

file       = h5py.File(path, 'r')
ds         = file['volumes/raw']
block_size = (32,) * 3
img, _     = imglyb.as_cell_img(ds, block_size, access_type='array', cache=10000)
try:
    vimg   = VolatileViews.wrapAsVolatile(img)
except Exception as e:
    print(scyjava.jstacktrace(e))
    raise e

bdv = BdvFunctions.show(vimg, 'raw')

def runUntilBdvDoesNotShow():
    panel = bdv.getBdvHandle().getViewerPanel()
    while panel.isShowing():
        time.sleep(0.3)


threading.Thread(target=runUntilBdvDoesNotShow).start()
