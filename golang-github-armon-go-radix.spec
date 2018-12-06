# http://github.com/armon/go-radix
%global goipath         github.com/armon/go-radix
Version:                1.0.0

%gometa

Name:           golang-github-armon-go-radix
Release:        1%{?dist}
Summary:        Golang implementation of Radix trees
License:        MIT
URL:            %{gourl}
Source0:        %{gosource}
Source1:        glide.yaml
Source2:        glide.lock

%description
%{summary}

%package devel
Summary:       %{summary}
BuildArch:     noarch

%description devel
%{summary}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.

%prep
%forgesetup
cp %{SOURCE1} %{SOURCE2} .

%install
%goinstall glide.lock glide.yaml

%check
%gochecks

#define license tag if not already defined
%{!?_licensedir:%global license %doc}

%files devel -f devel.file-list
%license LICENSE
%doc README.md

%changelog
* Mon Nov 12 2018 Robert-André Mauchin <zebob.m@gmail.com> - 1.0.0-1
- Release 1.0.0

* Tue Oct 23 2018 Nicolas Mailhot <nim@fedoraproject.org> - 0-0.16.git4239b77
- redhat-rpm-config-123 triggers bugs in gosetup, remove it from Go spec files as it’s just an alias
- https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/RWD5YATAYAFWKIDZBB7EB6N5DAO4ZKFM/

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.15.git4239b77
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 08 2018 Jan Chaloupka <jchaloup@redhat.com> - 0-0.14.git4239b77
- Upload glide.lock and glide.yaml

* Sun Mar 18 2018 Jan Chaloupka <jchaloup@redhat.com> - 0-0.13.git4239b77
- Bump to 4239b77079c7b5d1243b7b4736304ce8ddb6f0f2

* Wed Feb 28 2018 Jan Chaloupka <jchaloup@redhat.com> - 0-0.12.20150603gitfbd82e8
- Autogenerate some parts using the new macros

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.11.gitfbd82e8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.10.gitfbd82e8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.9.gitfbd82e8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.8.gitfbd82e8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jul 21 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.7.gitfbd82e8
- https://fedoraproject.org/wiki/Changes/golang1.7

* Mon Feb 22 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.6.gitfbd82e8
- https://fedoraproject.org/wiki/Changes/golang1.6

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.5.gitfbd82e8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jan 06 2016 Fridolin Pokorny <fpokorny@redhat.com> - 0-0.4.gitfbd82e8
- Bump to upstream fbd82e84e2b13651f3abc5ffd26b65ba71bc8f93
  related: #1248654

* Sat Sep 12 2015 jchaloup <jchaloup@redhat.com> - 0-0.3.git0bab926
- Update to spec-2.1
  related: #1248654

* Thu Jul 30 2015 Fridolin Pokorny <fpokorny@redhat.com> - 0-0.2.git0bab926
- Update of spec file to spec-2.0
  resolves: #1248654

* Wed Apr 15 2015 jchaloup <jchaloup@redhat.com> - 0-0.1.git0bab926
- First package for Fedora
  resolves: #1212004

