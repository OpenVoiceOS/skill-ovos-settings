#!/usr/bin/env python3
from setuptools import setup

# skill_id=package_name:SkillClass
PLUGIN_ENTRY_POINT = 'skill-ovos-settings.openvoiceos=ovos_skill_settings:OpenVoiceOSSettings'

setup(
    # this is the package name that goes on pip
    name='ovos-skill-settings',
    version='0.0.1',
    description='OVOS settings skill plugin',
    url='https://github.com/OpenVoiceOS/skill-ovos-settings',
    author='JarbasAi',
    author_email='jarbasai@mailfence.com',
    license='Apache-2.0',
    package_dir={"ovos_skill_settings": ""},
    package_data={'ovos_skill_settings': ["locale/*", "dialog/*", "vocab/*", "ui/*", "res/*", ]},
    packages=['ovos_skill_settings'],
    include_package_data=True,
    keywords='ovos skill plugin',
    entry_points={'ovos.plugin.skill': PLUGIN_ENTRY_POINT}
)
