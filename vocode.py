#!/usr/bin/env python

# imports and requirements
import gtk, gst, sys, socket, gobject
gobject.threads_init()

# auto speech recognizer
class vocode(object):

    def __init__(self):
        self.init_gst()
        self.pipeline.set_state(gst.STATE_PLAYING)

        # socket
        self.sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect(("127.0.0.1", 2222))

    def init_gst(self):
        self.pipeline = gst.parse_launch('alsasrc ! ' +
            'audioconvert ! ' +
            'audioresample ! ' +
            'vader name=vad auto-threshold=true ! ' +
            'pocketsphinx name=asr ! ' +
            'fakesink')

        asr = self.pipeline.get_by_name('asr')
        asr.connect('result', self.result)
        asr.set_property('lm', 'corpus/lm')
        asr.set_property('dict', 'corpus/dic')
        asr.set_property('configured', True)

        bus = self.pipeline.get_bus()
        bus.add_signal_watch()
        bus.connect('message::application', self.messenger)
        self.pipeline.set_state(gst.STATE_PAUSED)

    def messenger(self, bus, msg):
        self.result(msg.structure['hyp'], msg.structure['uttid'])

    def result(self, asr, hyp, uttid):
        if hyp == "STOP VOCODE":
            self.quit()
        self.sock.sendall(hyp)

    def stop(self):
        self.sock.sendall("-1")
        self.sock.close()
        sys.exit()

if __name__ == '__main__':
    asr = vocode()
    try:
        gtk.main()   
    except:
        asr.stop()