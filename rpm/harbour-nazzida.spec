# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.32
# 

Name:       harbour-nazzida

# >> macros
%define __provides_exclude_from ^%{_datadir}/.*$
%define __requires_exclude ^libFirfuoridaQt5|libHbnSfosComponentsQt5.*$
# << macros

Summary:    Personal Fluid Balance Protocol
Version:    1.0.1
Release:    1
Group:      Applications/Databases
License:    GPL-3.0-or-later
URL:        https://github.com/Huessenbergnetz/nazzida
Source0:    %{name}-%{version}.tar.bz2
Source100:  harbour-nazzida.yaml
Requires:   sailfishsilica-qt5 >= 0.10.9
BuildRequires:  pkgconfig(sailfishapp) >= 1.0.2
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  pkgconfig(Qt5Quick)
BuildRequires:  pkgconfig(Qt5Sql)
BuildRequires:  pkgconfig(sailfishsilica)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  librsvg-tools
BuildRequires:  bc
BuildRequires:  qt5-qttools-linguist
BuildRequires:  desktop-file-utils
BuildRequires:  cmake

%description
Nazzida is the old high german word for liquid. This applicaton helps you to manage a personal fluid balance protocol if you need to log your daily liquid input and output.


%prep
%setup -q -n %{name}-%{version}

# >> setup
# << setup

%build
# >> build pre
# << build pre

%cmake . 
make %{?_smp_mflags}

# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
# << install pre
%make_install

# >> install post
# << install post

desktop-file-install --delete-original       \
  --dir %{buildroot}%{_datadir}/applications             \
   %{buildroot}%{_datadir}/applications/*.desktop

%files
%defattr(-,root,root,-)
%{_bindir}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
# >> files
%exclude %{_bindir}/firfuorida
%exclude %{_datadir}/%{name}/lib/cmake
%exclude %{_includedir}/firfuorida-qt5
# << files
