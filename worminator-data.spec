Name:           worminator-data
Version:        3.0R2.1
Release:        %mkrel 4
Summary:        Data for Worminator
Group:          Games/Arcade
License:        GPLv2+
URL:            http://sourceforge.net/projects/worminator/
Source0:        http://download.sourceforge.net/worminator/%{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}
BuildArch:      noarch

%description
Data for Worminator, a game where you play as The Worminator and fight your
way through many levels of madness and mayhem. Worminator features nine unique
weapons, visible character damage, full screen scrolling, sound and music, and
much more!

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_datadir}/worminator
tar xzf %{SOURCE0} -C %{buildroot}%{_datadir}/worminator
rm %{buildroot}%{_datadir}/worminator/ICON.ICO

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_datadir}/worminator

