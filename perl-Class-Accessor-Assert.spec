%define upstream_name    Class-Accessor-Assert
%define upstream_version 1.40

Name:           perl-%{upstream_name}
Version:        %perl_convert_version %{upstream_version}
Release:        %mkrel 1

Summary:        Accessors which type-check
License:        GPL+ or Artistic
Group:		    Development/Perl
URL:            http://search.cpan.org/dist/%{upstream_name}
Source0:        http://www.cpan.org/modules/by-module/Class/%{upstream_name}-%{upstream_version}.tar.bz2

%if %{mdkversion} < 1010
Buildrequires:  perl-devel
%endif
BuildRequires:	perl(Class::Accessor)
BuildRequires:	perl(Class::Data::Inheritable)
BuildArch:	    noarch
BuildRoot:	    %{_tmppath}/%{name}-%{version}-%{release}

%description
This is a version of Class::Accessor which offers rudimentary
type-checking and existence-checking of arguments to constructors and
set accessors.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}
chmod 644 README Changes

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/Class
%{_mandir}/*/*
