%define name glpi-plugin-reports
%define version 1.4.0
%define release %mkrel 1

Summary: SNMP agent plugin
Name: %{name}
Version: %{version}
Release: %{release}
License: GPL
Group: Monitoring
Url: https://forge.indepnet.net/projects/reports
Source0: https://forge.indepnet.net/attachments/download/136/glpi-reports-%{version}.tar.gz
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}

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

%install
rm -rf %{buildroot}

install -d -m 755 %{buildroot}%{_datadir}/glpi/plugins/reports
cp -ap * %{buildroot}%{_datadir}/glpi/plugins/reports
rm -rf %{buildroot}%{_datadir}/glpi/plugins/reports/docs

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc docs/*
%{_datadir}/glpi/plugins/reports
