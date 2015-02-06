%if %mandriva_branch == Cooker
%define release 3
%else
%define subrel 1
%define release 1
%endif

Summary: SNMP agent plugin
Name: glpi-plugin-reports
Version: 1.5.0
Release: %{release}
License: GPL
Group: Monitoring
Url: https://forge.indepnet.net/projects/reports
Source0: https://forge.indepnet.net/attachments/download/926/glpi-reports-%{version}.tar.gz
BuildArch: noarch

%description
This plugin enables additional reports.

Main features :
* It also plugin allow you to add new reports in a simply way (one PHP script
  for the report and one for the translation).
* It handle the right for each new report
* It provides some new reports (as sample)


This plugin allows you to create bays. Manage the placement of your materials
in your bays. And so know the space and its power consumption and heat
dissipation.

%prep

%setup -q -n reports

find . -type f | xargs chmod 644
find . -type d | xargs chmod 755

%install

install -d -m 755 %{buildroot}%{_datadir}/glpi/plugins/reports
cp -ap * %{buildroot}%{_datadir}/glpi/plugins/reports
rm -rf %{buildroot}%{_datadir}/glpi/plugins/reports/docs

%files
%doc docs/*
%{_datadir}/glpi/plugins/reports


%changelog
* Sat Feb 04 2012 Oden Eriksson <oeriksson@mandriva.com> 1.5.0-2mdv2012.0
+ Revision: 771132
- various fixes

* Sat Feb 04 2012 Oden Eriksson <oeriksson@mandriva.com> 1.5.0-1
+ Revision: 771092
- 1.5.0

* Fri May 27 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.4.0-1
+ Revision: 680280
- new version

* Fri Jul 30 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.3.0-1mdv2011.0
+ Revision: 563563
- import glpi-plugin-reports


