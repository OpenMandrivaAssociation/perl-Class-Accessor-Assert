%define module  Class-Accessor-Assert
%define name    perl-%{module}
%define version 1.40
%define release %mkrel 2

Name:           %{name}
Version:        %{version}
Release:        %{release}
Summary:        Accessors which type-check
License:        GPL or Artistic
Group:		    Development/Perl
URL:            http://search.cpan.org/dist/%{module}
Source:         http://www.cpan.org/modules/by-module/Class/%{module}-%{version}.tar.bz2
%if %{mdkversion} < 1010
Buildrequires:  perl-devel
%endif
BuildRequires:	perl(Class::Accessor)
BuildRequires:	perl(Class::Data::Inheritable)
BuildArch:	    noarch
BuildRoot:	    %{_tmppath}/%{name}-%{version}

%description
This is a version of Class::Accessor which offers rudimentary
type-checking and existence-checking of arguments to constructors and
set accessors.

%prep
%setup -q -n %{module}-%{version} 
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


