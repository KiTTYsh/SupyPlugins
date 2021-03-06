###
# Copyright (c) 2014, James Lu (GLolol)
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
#   * Redistributions of source code must retain the above copyright notice,
#     this list of conditions, and the following disclaimer.
#   * Redistributions in binary form must reproduce the above copyright notice,
#     this list of conditions, and the following disclaimer in the
#     documentation and/or other materials provided with the distribution.
#   * Neither the name of the author of this software nor the name of
#     contributors to this software may be used to endorse or promote products
#     derived from this software without specific prior written consent.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED.  IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

###

from sys import version_info
from supybot.test import *

class SupyMiscTestCase(PluginTestCase):
    plugins = ('SupyMisc',)

    def setUp(self):
        PluginTestCase.setUp(self)
        self.prefix = 'foo!bar@baz.not'

    def testTld(self):
        self.assertNotError('tld .com')

    def testTldInternationalTLDs(self):
        # https://www.iana.org/domains/root/db/xn--io0a7i
        # Chinese internationalized domain for 'network' (similar to .net)
        self.assertNotError('tld xn--io0a7i')
        if version_info[0] >= 3:
            self.assertNotError('tld \u7f51\u7edc')
        else:
            from codecs import unicode_escape_decode as u
            self.assertNotError('tld '+u('\u7f51\u7edc')[0])

    def testColorwheel(self):
        self.assertRegexp('colors', '.*\x03.*')

    def testHostFetchers(self):
        self.assertResponse('me', 'foo')
        self.assertResponse('getident', 'bar')
        self.assertResponse('gethost', 'baz.not')
        self.assertResponse('botnick', self.nick)

    def testmreplace(self):
        self.assertResponse('mreplace hi,there hello,ok hmm, hi there everyone',
            'hmm, hello ok everyone')

    def testSPsourceFetch(self):
        self.assertNotError('supyplugins')
        self.assertRegexp('supyplugins SupyMisc//plugin.py', \
            '.*?blob\/master\/SupyMisc\/plugin\.py.*?')
        self.assertRegexp('supyplugins SupyMisc/', \
            '.*?tree\/master\/SupyMisc.*?')
        self.assertError('supyplugins asfswfuiahfawfawefawe')


# vim:set shiftwidth=4 tabstop=4 expandtab textwidth=79:
