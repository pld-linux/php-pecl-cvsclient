%define		_modname	cvsclient
%define		_status		beta

Summary:	%{_modname} - CVS pserver client
Summary(pl):	%{_modname} - klient CVS pserver
Name:		php-pecl-%{_modname}
Version:	0.2
Release:	1
License:	PHP
Group:		Development/Languages/PHP
Source0:	http://pecl.php.net/get/%{_modname}-%{version}.tgz
# Source0-md5:	d25ca6d7797118edf37817fcb7e93bc7
URL:		http://pecl.php.net/package/cvsclient/
BuildRequires:	libtool
BuildRequires:	php-devel
Requires:	php-common
Obsoletes:	php-pear-%{_modname}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/php
%define		extensionsdir	%{_libdir}/php

%description
pserver client extension. Current version has read-only streams wrapper.
Later versions to include commit/diff/log support.

In PECL status of this package is: %{_status}.

%description -l pl
Modu³ klienta CVS pserver. Na chwilê obecn± dostêpne jest wsparcie tylko
'read only'. W nastêpnych wersjach planowane jest wsparcie dla komend
commit/diff/log.

To rozszerzenie ma w PECL status: %{_status}.

%prep
%setup -q -c

%build
cd %{_modname}-%{version}
phpize
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{extensionsdir}

install %{_modname}-%{version}/modules/%{_modname}.so $RPM_BUILD_ROOT%{extensionsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%{_sbindir}/php-module-install install %{_modname} %{_sysconfdir}/php-cgi.ini

%preun
if [ "$1" = "0" ]; then
	%{_sbindir}/php-module-install remove %{_modname} %{_sysconfdir}/php-cgi.ini
fi

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/%{_modname}.so
