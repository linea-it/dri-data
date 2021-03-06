#!/usr/bin/env python
# -*- coding: utf-8 -*-

import simplejson
from tools.portaldb import PortalDB


class SurveyExport():

    def __init__(self, database):

        self.db = database

    def get_django_data(self):
        json_string = u'''[
    {
        "model":"coadd.survey",
        "pk":1,
        "fields":{
            "srv_release":1,
            "srv_filter":2,
            "srv_project":"DES",
            "srv_display_name":"Y1 Wide Survey - g",
            "srv_url":"http://desportal.cosmology.illinois.edu/data/releases/y1_wide_survey/images/aladin/g",
            "srv_target":"21 33 27.002 -00 48 24.64",
            "srv_fov":0.3
        }
    },
    {
        "model":"coadd.survey",
        "pk":2,
        "fields":{
            "srv_release":1,
            "srv_filter":3,
            "srv_project":"DES",
            "srv_display_name":"Y1 Wide Survey - r",
            "srv_url":"http://desportal.cosmology.illinois.edu/data/releases/y1_wide_survey/images/aladin/r",
            "srv_target":"21 33 27.002 -00 48 24.64",
            "srv_fov":0.3
        }
    },
    {
        "model":"coadd.survey",
        "pk":3,
        "fields":{
            "srv_release":1,
            "srv_filter":4,
            "srv_project":"DES",
            "srv_display_name":"Y1 Wide Survey - i",
            "srv_url":"http://desportal.cosmology.illinois.edu/data/releases/y1_wide_survey/images/aladin/i",
            "srv_target":"21 33 27.002 -00 48 24.64",
            "srv_fov":0.3
        }
    },
    {
        "model":"coadd.survey",
        "pk":4,
        "fields":{
            "srv_release":1,
            "srv_filter":5,
            "srv_project":"DES",
            "srv_display_name":"Y1 Wide Survey - z",
            "srv_url":"http://desportal.cosmology.illinois.edu/data/releases/y1_wide_survey/images/aladin/z",
            "srv_target":"21 33 27.002 -00 48 24.64",
            "srv_fov":0.3
        }
    },
    {
        "model":"coadd.survey",
        "pk":5,
        "fields":{
            "srv_release":1,
            "srv_filter":6,
            "srv_project":"DES",
            "srv_display_name":"Y1 Wide Survey - Y",
            "srv_url":"http://desportal.cosmology.illinois.edu/data/releases/y1_wide_survey/images/aladin/y",
            "srv_target":"21 33 27.002 -00 48 24.64",
            "srv_fov":0.3
        }
    },
    {
        "model":"coadd.survey",
        "pk":6,
        "fields":{
            "srv_release":1,
            "srv_filter":7,
            "srv_project":"DES",
            "srv_display_name":"Y1 Wide Survey - irg",
            "srv_url":"http://desportal.cosmology.illinois.edu/data/releases/y1_wide_survey/images/aladin/irg",
            "srv_target":"21 33 27.002 -00 48 24.64",
            "srv_fov":0.3
        }
    },
    {
        "model":"coadd.survey",
        "pk":7,
        "fields":{
            "srv_release":2,
            "srv_filter":2,
            "srv_project":"DES",
            "srv_display_name":"Y1 Suplemental D04 - g",
            "srv_url":"http://desportal.cosmology.illinois.edu/data/releases/y1_supplemental_d04/images/aladin/g",
            "srv_target":null,
            "srv_fov":null
        }
    },
    {
        "model":"coadd.survey",
        "pk":8,
        "fields":{
            "srv_release":2,
            "srv_filter":3,
            "srv_project":"DES",
            "srv_display_name":"Y1 Suplemental D04 - r",
            "srv_url":"http://desportal.cosmology.illinois.edu/data/releases/y1_supplemental_d04/images/aladin/r",
            "srv_target":null,
            "srv_fov":null
        }
    },
    {
        "model":"coadd.survey",
        "pk":9,
        "fields":{
            "srv_release":2,
            "srv_filter":4,
            "srv_project":"DES",
            "srv_display_name":"Y1 Suplemental D04 - i",
            "srv_url":"http://desportal.cosmology.illinois.edu/data/releases/y1_supplemental_d04/images/aladin/i",
            "srv_target":null,
            "srv_fov":null
        }
    },
    {
        "model":"coadd.survey",
        "pk":10,
        "fields":{
            "srv_release":2,
            "srv_filter":5,
            "srv_project":"DES",
            "srv_display_name":"Y1 Suplemental D04 - z",
            "srv_url":"http://desportal.cosmology.illinois.edu/data/releases/y1_supplemental_d04/images/aladin/z",
            "srv_target":null,
            "srv_fov":null
        }
    },
    {
        "model":"coadd.survey",
        "pk":11,
        "fields":{
            "srv_release":2,
            "srv_filter":6,
            "srv_project":"DES",
            "srv_display_name":"Y1 Suplemental D04 - Y",
            "srv_url":"http://desportal.cosmology.illinois.edu/data/releases/y1_supplemental_d04/images/aladin/y",
            "srv_target":null,
            "srv_fov":null
        }
    },
    {
        "model":"coadd.survey",
        "pk":12,
        "fields":{
            "srv_release":2,
            "srv_filter":7,
            "srv_project":"DES",
            "srv_display_name":"Y1 Suplemental D04 - irg",
            "srv_url":"http://desportal.cosmology.illinois.edu/data/releases/y1_supplemental_d04/images/aladin/irg",
            "srv_target":"02 21 36.570 -05 31 15.33",
            "srv_fov":0.1
        }
    },
    {
        "model":"coadd.survey",
        "pk":13,
        "fields":{
            "srv_release":3,
            "srv_filter":2,
            "srv_project":"DES",
            "srv_display_name":"Y1 Suplemental D10 - g",
            "srv_url":"http://desportal.cosmology.illinois.edu/data/releases/y1_supplemental_d10/images/aladin/g",
            "srv_target":null,
            "srv_fov":null
        }
    },
    {
        "model":"coadd.survey",
        "pk":14,
        "fields":{
            "srv_release":3,
            "srv_filter":3,
            "srv_project":"DES",
            "srv_display_name":"Y1 Suplemental D10 - r",
            "srv_url":"http://desportal.cosmology.illinois.edu/data/releases/y1_supplemental_d10/images/aladin/r",
            "srv_target":null,
            "srv_fov":null
        }
    },
    {
        "model":"coadd.survey",
        "pk":15,
        "fields":{
            "srv_release":3,
            "srv_filter":4,
            "srv_project":"DES",
            "srv_display_name":"Y1 Suplemental D10 - i",
            "srv_url":"http://desportal.cosmology.illinois.edu/data/releases/y1_supplemental_d10/images/aladin/i",
            "srv_target":null,
            "srv_fov":null
        }
    },
    {
        "model":"coadd.survey",
        "pk":16,
        "fields":{
            "srv_release":3,
            "srv_filter":5,
            "srv_project":"DES",
            "srv_display_name":"Y1 Suplemental D10 - z",
            "srv_url":"http://desportal.cosmology.illinois.edu/data/releases/y1_supplemental_d10/images/aladin/z",
            "srv_target":null,
            "srv_fov":null
        }
    },
    {
        "model":"coadd.survey",
        "pk":17,
        "fields":{
            "srv_release":3,
            "srv_filter":6,
            "srv_project":"DES",
            "srv_display_name":"Y1 Suplemental D10 - Y",
            "srv_url":"http://desportal.cosmology.illinois.edu/data/releases/y1_supplemental_d10/images/aladin/y",
            "srv_target":null,
            "srv_fov":null
        }
    },
    {
        "model":"coadd.survey",
        "pk":18,
        "fields":{
            "srv_release":3,
            "srv_filter":7,
            "srv_project":"DES",
            "srv_display_name":"Y1 Suplemental D10 - irg",
            "srv_url":"http://desportal.cosmology.illinois.edu/data/releases/y1_supplemental_d10/images/aladin/irg",
            "srv_target":null,
            "srv_fov":null
        }
    },
    {
        "model":"coadd.survey",
        "pk":19,
        "fields":{
            "srv_release":4,
            "srv_filter":2,
            "srv_project":"DES",
            "srv_display_name":"Y1 Suplemental DFULL - g",
            "srv_url":"http://desportal.cosmology.illinois.edu/data/releases/y1_supplemental_dfull/images/aladin/g",
            "srv_target":null,
            "srv_fov":null
        }
    },
    {
        "model":"coadd.survey",
        "pk":20,
        "fields":{
            "srv_release":4,
            "srv_filter":3,
            "srv_project":"DES",
            "srv_display_name":"Y1 Suplemental DFULL - r",
            "srv_url":"http://desportal.cosmology.illinois.edu/data/releases/y1_supplemental_dfull/images/aladin/r",
            "srv_target":null,
            "srv_fov":null
        }
    },
    {
        "model":"coadd.survey",
        "pk":21,
        "fields":{
            "srv_release":4,
            "srv_filter":4,
            "srv_project":"DES",
            "srv_display_name":"Y1 Suplemental DFULL - i",
            "srv_url":"http://desportal.cosmology.illinois.edu/data/releases/y1_supplemental_dfull/images/aladin/i",
            "srv_target":null,
            "srv_fov":null
        }
    },
    {
        "model":"coadd.survey",
        "pk":22,
        "fields":{
            "srv_release":4,
            "srv_filter":5,
            "srv_project":"DES",
            "srv_display_name":"Y1 Suplemental DFULL - z",
            "srv_url":"http://desportal.cosmology.illinois.edu/data/releases/y1_supplemental_dfull/images/aladin/z",
            "srv_target":null,
            "srv_fov":null
        }
    },
    {
        "model":"coadd.survey",
        "pk":23,
        "fields":{
            "srv_release":4,
            "srv_filter":6,
            "srv_project":"DES",
            "srv_display_name":"Y1 Suplemental DFULL - Y",
            "srv_url":"http://desportal.cosmology.illinois.edu/data/releases/y1_supplemental_dfull/images/aladin/y",
            "srv_target":null,
            "srv_fov":null
        }
    },
    {
        "model":"coadd.survey",
        "pk":24,
        "fields":{
            "srv_release":4,
            "srv_filter":7,
            "srv_project":"DES",
            "srv_display_name":"Y1 Suplemental DFULL - irg",
            "srv_url":"http://desportal.cosmology.illinois.edu/data/releases/y1_supplemental_dfull/images/aladin/irg",
            "srv_target":null,
            "srv_fov":null
        }
    }
]'''

        return simplejson.loads(json_string)


if __name__ == '__main__':

    db = PortalDB(
        config_key=None,
        dburl="postgres://fnaldba:dbafnal@localhost/fnal",
        debug=False
    )

    export = SurveyExport(db)
    file = open("json/survey.json", "w")
    file.write(simplejson.dumps(export.get_django_data(), ensure_ascii=False))
    file.close()
