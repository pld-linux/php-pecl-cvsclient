%define		_modname	cvsclient
%define		_status		beta
Summary:	%{_modname} - CVS pserver client
Summary(pl.UTF-8):	%{_modname} - klient CVS pserver
Name:		php-pecl-%{_modname}
Version:	0.2
Release:	5
License:	PHP
Group:		Development/Languages/PHP
Source0:	http://pecl.php.net/get/%{_modname}-%{version}.tgz
# Source0-md5:	d25ca6d7797118edf37817fcb7e93bc7
URL:		http://pecl.php.net/package/cvsclient/
BuildRequires:	php-devel >= 3:5.0.0
BuildRequires:	rpmbuild(macros) >= 1.344
%{?requires_php_extension}
Requires:	php-common >= 4:5.0.4
Obsoletes:	php-pear-%{_modname}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
pserver client extension. Current version has read-only streams
wrapper. Later versions to include commit/diff/log support.

In PECL status of this package is: %{_status}.

%description -l pl.UTF-8
Moduł klienta CVS pserver. Na chwilę obecną dostępne jest wsparcie
tylko 'read only'. W następnych wersjach planowane jest wsparcie dla
komend commit/diff/log.

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
install -d $RPM_BUILD_ROOT{%{php_sysconfdir}/conf.d,%{php_extensiondir}}

install %{_modname}-%{version}/modules/%{_modname}.so $RPM_BUILD_ROOT%{php_extensiondir}
cat <<'EOF' > $RPM_BUILD_ROOT%{php_sysconfdir}/conf.d/%{_modname}.ini
; Enable %{_modname} extension module
extension=%{_modname}.so
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%post
%php_webserver_restart

%postun
if [ "$1" = 0 ]; then
	%php_webserver_restart
fi

%files
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{php_sysconfdir}/conf.d/%{_modname}.ini
%attr(755,root,root) %{php_extensiondir}/%{_modname}.so
