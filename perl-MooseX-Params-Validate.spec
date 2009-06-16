#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	MooseX
%define	pnam	Params-Validate
Summary:	MooseX::Params::Validate - an extension of Params::Validate for using Moose's types
#Summary(pl.UTF-8):	
Name:		perl-MooseX-Params-Validate
Version:	0.09
Release:	1
License:	Perl
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/MooseX/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	32f356facb51480c1f12d485e749cd08
URL:		http://search.cpan.org/dist/MooseX-Params-Validate/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Moose >= 0.58
BuildRequires:	perl-Params-Validate >= 0.88
BuildRequires:	perl-Sub-Exporter
BuildRequires:	perl-Test-Exception >= 0.21
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module fills a gap in Moose by adding method parameter validation
to Moose. This is just one of many developing options, it should not
be considered the "official" one by any means though.

You might also want to explore MooseX::Method::Signatures and
MooseX::Declare



# %description -l pl.UTF-8
# TODO

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

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%{perl_vendorlib}/MooseX/Params/*.pm
%{_mandir}/man3/*
