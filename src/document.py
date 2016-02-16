#!/usr/bin/python3

import os
from gi.repository import Gdk, GdkPixbuf, Poppler
import cairo

class document:

	def __init__(self, filepath):
		self.filepath = filepath
		self.popplerdocument = Poppler.Document.new_from_file('file://' + self.filepath, None)

	def document_get_name(self):
		return os.path.basename(self.filepath)

	def document_get_directory(self):
		return self.filepath.replace("/"+os.path.basename(self.filepath),"")

	def document_get_pagecount(self):
		return self.popplerdocument.get_n_pages()

	def page_export_pdf(self, page):
		pass

	def page_get_thumbnail(self, page):
		page = self.popplerdocument.get_page(page)
		#page = pdf.get_page(3)
		width, height = page.get_size()
		#page.RenderToPixbuf(pixbuf)
		#surface = cairo.PDFSurface(page, width, height)
		#ctx = cairo.Context(surface)
		surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, int(width), int(height))
		ctx = cairo.Context(surface)
		page.render(ctx)
		img = Gdk.pixbuf_get_from_surface(ctx.get_target(), 0, 0, ctx.get_target().get_width(), ctx.get_target().get_height())
		#output = cairo.PDFSurface(survey.path('annotated_questionnaire.pdf'), 2*width, 2*height)
		#cr = cairo.Context(output)
		#pixbuf = GdkPixbuf.Pixbuf.new_from_file('test2.jpg')
		return img.scale_simple(100, 150, GdkPixbuf.InterpType.HYPER)

	# PAGE_SET
	def page_set_crop(self, page):
		pass

	def page_set_roation(self, page):
		pass

	def page_set_scale(self, page):
		pass

	def page_set_enhance(self, page):
		pass