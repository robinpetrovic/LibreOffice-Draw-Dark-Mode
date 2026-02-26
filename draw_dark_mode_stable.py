import uno
from com.sun.star.awt import Point, Size

bg_is_dark = False
BG_SHAPE_NAME = "_dark_bg"

def toggle_dark_mode(*args):
    global bg_is_dark

    ctx = uno.getComponentContext()
    smgr = ctx.ServiceManager
    desktop = smgr.createInstanceWithContext("com.sun.star.frame.Desktop", ctx)
    doc = desktop.getCurrentComponent()

    if not doc.supportsService("com.sun.star.drawing.DrawingDocument"):
        return

    bg_color = 0x1A1A1A if not bg_is_dark else 0xFFFFFF
    text_color = 0xFFFFFF if not bg_is_dark else 0x000000

    for page in doc.getDrawPages():
        bg_shape = None
        for shape in page:
            if shape.getName() == BG_SHAPE_NAME:
                bg_shape = shape
                break

        if bg_shape is None:
            width = page.Width
            height = page.Height
            bg_shape = doc.createInstance("com.sun.star.drawing.RectangleShape")
            bg_shape.setSize(Size(width, height))
            bg_shape.setPosition(Point(0,0))
            bg_shape.setName(BG_SHAPE_NAME)
            page.add(bg_shape)

        bg_shape.FillColor = bg_color
        bg_shape.ZOrder = 0

        for shape in page:
            if shape.getName() == BG_SHAPE_NAME:
                continue
            if shape.supportsService("com.sun.star.drawing.TextShape"):
                shape.CharColor = text_color
                try:
                    cursor = shape.createTextCursor()
                    cursor.gotoStart(False)
                    cursor.gotoEnd(True)
                    cursor.CharColor = text_color
                except:
                    pass

    bg_is_dark = not bg_is_dark
