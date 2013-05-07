#!/usr/bin/env python
import json
from libnmap.common import NmapHost, NmapService
from libnmap.report import NmapReport
from libnmap.parser import NmapParser


class ReportEncoder(json.JSONEncoder):
    def default(self, obj):
        otype = {'NmapHost': NmapHost,
                 'NmapService': NmapService,
                 'NmapReport': NmapReport}
        if isinstance(obj, tuple(otype.values())):
            key = '__%s__' % obj.__class__.__name__
            return {key: obj.__dict__}
        return json.JSONEncoder.default(self, obj)


class ReportDecoder(json.JSONDecoder):
    def decode(self, json_str):
        raw_data = NmapParser.parse_fromdict(json.loads(json_str))
        r = NmapReport(name=raw_data['_name'], raw_data=raw_data)
        return r
