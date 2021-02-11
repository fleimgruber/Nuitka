#     Copyright 2020, Kay Hayen, mailto:kay.hayen@gmail.com
#
#     Part of "Nuitka", an optimizing Python compiler that is compatible and
#     integrates with CPython, but also works on its own.
#
#     Licensed under the Apache License, Version 2.0 (the "License");
#     you may not use this file except in compliance with the License.
#     You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#     Unless required by applicable law or agreed to in writing, software
#     distributed under the License is distributed on an "AS IS" BASIS,
#     WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#     See the License for the specific language governing permissions and
#     limitations under the License.
#
""" Standard plug-in to make pkg_resources module work when compiled.

The pkg_resources module needs to be able to use the Nuitka loader to find
resources on behalf of compiled modules.
"""

from nuitka.plugins.PluginBase import NuitkaPluginBase


class NuitkaPluginPkgResourcesLoader(NuitkaPluginBase):
    """This is to make pkg_resources module work when compiled with Nuitka."""

    plugin_name = "pkg_resources"

    @classmethod
    def isRelevant(cls):
        return True

    @staticmethod
    def isAlwaysEnabled():
        return True

    @staticmethod
    def createPostModuleLoadCode(module):
        full_name = module.getFullName()

        if full_name == "pkg_resources":
            code = """\
from __future__ import absolute_import
import pkg_resources
try:
    print(__loader__)
    # pkg_resources.register_loader_type(__loader__, pkg_resources.DefaultProvider)
except AttributeError:
    pass
"""
            return (
                code,
                """\
Registering the Nuitka loader for "pkg_resources".""",
            )

        return None, None
