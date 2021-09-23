import scyjava

from jpype import JImplements, JOverride

__all__ = (
    'options2D'
)

def _java_setup():
    """
    Lazy initialization function for Java-dependent data structures.
    Do not call this directly; use scyjava.start_jvm() instead.
    """

    # bigdataviewer
    global BdvFunctions
    BdvFunctions = scyjava.jimport('bdv.util.BdvFunctions')
    global BdvOptions
    BdvOptions   = scyjava.jimport('bdv.util.BdvOptions')


    global GenericOverlayRenderer
    @JImplements('bdv.viewer.OverlayRenderer')
    class GenericOverlayRenderer():

        def __init__(self, draw_overlays=lambda g: None, set_canvas_size=lambda w, h: None):
            self.draw_overlays = draw_overlays
            self.set_canvas_size = set_canvas_size

        @JOverride
        def drawOverlays(self, g):
            self.draw_overlays(g)

        @JOverride
        def setCanvasSize(self, width, height):
            self.set_canvas_size(width, height)


scyjava.when_jvm_starts(_java_setup)

def options2D():
    scyjava.start_jvm()
    return BdvOptions.options().is2D()
