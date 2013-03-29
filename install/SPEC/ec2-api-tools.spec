%define _unpackaged_files_terminate_build 0
%define _target_os linux
%define project_version 1.6.7.1 
%define _binaries_in_noarch_packages_terminate_build   0
Name: ec2-api-tools 
Version: 1.6.7 
Release: 1 
Summary: Packaged version of the Amazon EC2 Command Lines Tools 
License: http://aws.amazon.com/terms/
Group: Aquto
Requires: java 
autoprov: yes
autoreq: yes
Prefix: /opt/ec2-api-tools

%description

%install
if [ -e $RPM_BUILD_ROOT ];
then
  rm -rf $RPM_BUILD_ROOT
fi
mkdir -p $RPM_BUILD_ROOT/%{prefix}/
mkdir -p $RPM_BUILD_ROOT/%{prefix}/install/bin

cp -R %{_projectdir}/lib/ $RPM_BUILD_ROOT%{prefix}/
cp -R %{_projectdir}/bin/  $RPM_BUILD_ROOT%{prefix}/
cp  %{_projectdir}/*.txt $RPM_BUILD_ROOT%{prefix}/
cp  %{_projectdir}/README $RPM_BUILD_ROOT%{prefix}/
cp  %{_projectdir}/install/bin/* $RPM_BUILD_ROOT%{prefix}/install/bin/

%files
%dir %{prefix}/*
%dir %{prefix}/bin/*
%dir %{prefix}/lib/*
%dir %{prefix}/install/bin/*


%pre

%post

%preun
if [ "$1" -eq "0" ]
then
rm -rf /etc/profile.d/ec2-api.sh
fi

%postun

%posttrans
cp %{prefix}/install/bin/ec2-api.sh /etc/profile.d/
