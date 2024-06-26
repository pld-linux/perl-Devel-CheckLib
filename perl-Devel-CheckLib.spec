#
# Conditional build:
%bcond_without	tests	# unit tests
#
%define		pdir	Devel
%define		pnam	CheckLib
Summary:	Devel::CheckLib - check that a library is available
Summary(pl.UTF-8):	Devel::CheckLib - sprawdzanie dostępności biblioteki
Name:		perl-Devel-CheckLib
Version:	1.16
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	https://www.cpan.org/modules/by-module/Devel/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	e0d362964e0371b9b0343c140aa40a81
URL:		https://metacpan.org/dist/Devel-CheckLib
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
%if %{with tests}
BuildRequires:	perl-Capture-Tiny
BuildRequires:	perl-File-Temp >= 0.16
BuildRequires:	perl-Mock-Config >= 0.02
BuildRequires:	perl-Test-Simple >= 0.88
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Devel::CheckLib is a Perl module that checks whether a particular C
library and its headers are available.

%description -l pl.UTF-8
Devel::CheckLib to moduł Perla sprawdzający, czy dana biblioteka C i
jej pliki nagłówkowe są dostępne.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

# remove deprecated script and its man page
%{__rm} $RPM_BUILD_ROOT%{_bindir}/use-devel-checklib
%{__rm} $RPM_BUILD_ROOT%{_mandir}/man1/use-devel-checklib.1*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README TODO
%{perl_vendorlib}/Devel/CheckLib.pm
%{_mandir}/man3/Devel::CheckLib.3pm*
