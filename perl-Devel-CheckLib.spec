#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	Devel
%define		pnam	CheckLib
%include	/usr/lib/rpm/macros.perl
Summary:	Devel::CheckLib - check that a library is available
Name:		perl-Devel-CheckLib
Version:	1.05
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Devel/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	c4792a4487ba54eb269f4783bf3a2fe6
URL:		http://search.cpan.org/dist/Devel-CheckLib/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(IO::CaptureOutput) >= 1.0801
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Devel::CheckLib is a perl module that checks whether a particular C
library and its headers are available.

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
%{_mandir}/man3/*
