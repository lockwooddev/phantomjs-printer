import envoy
import logging
import os
from urlparse import urlparse
import uuid

from django.utils.encoding import iri_to_uri

from .settings import TMP_STORAGE_FOLDER, TOKEN_NAME, TOKEN_VALUE

logger = logging.getLogger('phantomjs_printer')


def create_url(url):
    view_url = iri_to_uri(url)
    parsed_url = urlparse(view_url)

    parameter_seperator = "?"
    if parsed_url.query:
        parameter_seperator = "&"

    view_url = "%s%s%s=%s" % (view_url, parameter_seperator, TOKEN_NAME, TOKEN_VALUE)
    return view_url


def create_pdf(url):
    view_url = create_url(url)

    outfile = os.path.join(TMP_STORAGE_FOLDER, '%s.pdf' % uuid.uuid4())

    command = 'phantomjs --load-plugins=yes %s/r.js %s %s' % (
    	os.path.dirname(__file__), view_url, outfile)
    
    logger.info('Creating pdf: %s' % command)
    r = envoy.run(command)
    logger.info('Finished pdf. Status: %s, StdOut: %s, StdErr: %s' 
    	% (r.status_code, r.std_out, r.std_err))

    if r.status_code != 0:
    	raise PDFCreationException(r.status_code, r.std_err)

    if os.path.exists(outfile):
        return outfile
    else:
        logger.error('Could not create pdf for view: %s, stdout: %s' %(url, r.std_out))
        raise PDFCreationException(-1, "File not found")


def check_token(request):
    return request.GET.get(TOKEN_NAME) == TOKEN_VALUE