%define upstream_name    Class-Accessor-Assert
%define upstream_version 1.41

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	Accessors which type-check
License:	GPL+ or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Class/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Class::Accessor)
BuildRequires:	perl(Class::Data::Inheritable)
BuildArch:	noarch

%description
This is a version of Class::Accessor which offers rudimentary
type-checking and existence-checking of arguments to constructors and
set accessors.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}
chmod 644 README Changes

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes README
%{perl_vendorlib}/Class
%{_mandir}/*/*


%changelog
* Sat May 28 2011 Funda Wang <fwang@mandriva.org> 1.410.0-2mdv2011.0
+ Revision: 680776
- mass rebuild

* Thu Mar 04 2010 Jérôme Quelin <jquelin@mandriva.org> 1.410.0-1mdv2011.0
+ Revision: 514096
- update to 1.41

* Tue Jul 28 2009 Jérôme Quelin <jquelin@mandriva.org> 1.400.0-1mdv2010.0
+ Revision: 402133
- rebuild using %%perl_convert_version

* Wed Jul 30 2008 Thierry Vignaud <tv@mandriva.org> 1.40-4mdv2009.0
+ Revision: 255840
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 1.40-2mdv2008.1
+ Revision: 136680
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Sep 15 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.40-2mdv2008.0
+ Revision: 86067
- rebuild


* Wed Sep 06 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.40-1mdv2007.0
- New version
- %%mkrel
- spec cleanup

* Tue Aug 16 2005 Guillaume Rousse <guillomovitch@mandriva.org> 1.30-1mdk
- new version
- fix sources url for rpmbuildupdate
- fix documentation perms

* Wed Jul 13 2005 Oden Eriksson <oeriksson@mandriva.com> 1.2-1mdk
- initial Mandriva package

