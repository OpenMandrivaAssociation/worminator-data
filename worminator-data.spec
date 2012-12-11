Name:           worminator-data
Version:        3.0R2.1
Release:        %mkrel 5
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



%changelog
* Wed Sep 09 2009 Thierry Vignaud <tvignaud@mandriva.com> 3.0R2.1-5mdv2010.0
+ Revision: 434977
- rebuild

* Sun Aug 03 2008 Thierry Vignaud <tvignaud@mandriva.com> 3.0R2.1-4mdv2009.0
+ Revision: 262150
- rebuild

* Wed Jul 30 2008 Thierry Vignaud <tvignaud@mandriva.com> 3.0R2.1-3mdv2009.0
+ Revision: 256384
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sat Oct 27 2007 Adam Williamson <awilliamson@mandriva.org> 3.0R2.1-1mdv2008.1
+ Revision: 102481
- correct group
- spec based on Fedora, thanks
- import worminator-data


