%define		pre	beta4
Summary:	diff with editing capabilities for binary files
Summary(pl.UTF-8):	Odpowiednik diffa dla plików binarnych z możliwością edycji
Name:		vbindiff
Version:	3.0
Release:	0.%{pre}.1
License:	GPL v2+
Group:		Applications/Editors
Source0:	http://www.cjmweb.net/vbindiff/%{name}-%{version}_%{pre}.tar.gz
# Source0-md5:	dbda80ef580e1a0975ef50b9aaa5210e
URL:		http://www.cjmweb.net/vbindiff/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libstdc++-devel
BuildRequires:	ncurses-ext-devel >= 5.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Visual Binary Diff (VBinDiff) displays files in hexadecimal and ASCII
(or EBCDIC). It can also display two files at once, and highlight the
differences between them. Unlike diff, it works well with large files
(up to 4 GB).

%description -l pl.UTF-8
Visual Binary Diff (VBinDiff) wyświetla pliki w postaci szestnaskowej
lub ASCII/EBCDIC. Może również wyświetlać dwa pliki jednocześnie
podświetlając różnice pomiędzy nimi. W przeciwieństwie do diffa, radzi
sobie dobrze z dużymi plikami (do 4 GB).

%prep
%setup -q -n %{name}-%{version}_%{pre}

%build
CXXFLAGS="%{rpmcflags} -I/usr/include/ncurses"
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%doc AUTHORS NEWS README
%{_mandir}/man1/*
